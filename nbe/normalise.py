import nbe.semantics as semantics
import nbe.syntax as syntax
import nbe.type_syntax as type_syntax
from nbe.name_generator import NameGenerator


def nbe(tau, term):
    generator = NameGenerator()
    return reify(generator, tau, meaning({}, term))


def reflect(generator, tau, term):
    if isinstance(tau, type_syntax.Arrow):
        return semantics.Lambda(
            lambda s: reflect(
                generator,
                tau.target,
                syntax.Apply(
                    term,
                    reify(
                        generator,
                        tau.source,
                        s))))
    if isinstance(tau, type_syntax.Product):
        return semantics.Pair(
            (reflect(
                generator, tau.first, syntax.Fst(term)), reflect(
                generator, tau.second, syntax.Snd(term))))
    if isinstance(tau, type_syntax.Basic):
        return semantics.Syntax(term)
    raise ValueError("Type and term do not match in `reflect`")


def reify(generator, tau, semantic):
    if isinstance(
            tau,
            type_syntax.Arrow) and isinstance(
            semantic,
            semantics.Lambda):
        identifier = generator.next()
        return syntax.Lambda(
            identifier,
            reify(
                generator,
                tau.target,
                semantic.function(
                    reflect(
                        generator,
                        tau.source,
                        syntax.Var(identifier)))))
    if isinstance(
            tau,
            type_syntax.Product) and isinstance(
            semantic,
            semantics.Pair):
        first, second = semantic.pair
        return syntax.Pair(
            reify(
                generator, tau.first, first), reify(
                generator, tau.second, second))
    if isinstance(
            tau,
            type_syntax.Basic) and isinstance(
            semantic,
            semantics.Syntax):
        return semantic.syntax
    raise ValueError("Type and term do not match in `reify`")


def meaning(context, term):
    if isinstance(term, syntax.Var):
        return context[term.identifier]
    if isinstance(term, syntax.Lambda):
        def inner(body):
            new_context = context.copy()
            new_context[term.identifier] = body
            return meaning(new_context, term.body)
        return semantics.Lambda(inner)
    if isinstance(term, syntax.Apply):
        function_meaning = meaning(context, term.term1)
        if isinstance(function_meaning, semantics.Lambda):
            return function_meaning.function(meaning(context, term.term2))
        raise ValueError("Cannot apply non-function in `meaning`")
    if isinstance(term, syntax.Pair):
        return semantics.Pair((
            meaning(
                context, term.term1), meaning(
                context, term.term2)))
    if isinstance(term, syntax.Fst):
        pair_meaning = meaning(context, term.term)
        if isinstance(pair_meaning, semantics.Pair):
            first, _ = pair_meaning.pair
            return first
        raise ValueError("Cannot take fst of non-pair in `meaning`")
    if isinstance(term, syntax.Snd):
        pair_meaning = meaning(context, term.term)
        if isinstance(pair_meaning, semantics.Pair):
            _, second = pair_meaning.pair
            return second
    raise ValueError("Invalid syntax in `meaning`")
