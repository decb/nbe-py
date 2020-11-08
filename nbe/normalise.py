import semantics
import syntax
import type_syntax
from name_generator import NameGenerator

def nbe(ty, term):
    generator = NameGenerator()
    return reify(generator, ty, meaning({}, term))

def reflect(generator, ty, term):
    if isinstance(ty, type_syntax.Arrow):
        return semantics.Lambda (lambda s : reflect(generator, ty.target, syntax.Apply(term, reify(generator, ty.source, s))))
    if isinstance(ty, type_syntax.Product):
        return semantics.Pair((reflect(generator, ty.first, syntax.Fst(term)), reflect(generator, ty.second, syntax.Snd(term))))
    if isinstance(ty, type_syntax.Basic):
        return semantics.Syntax(term)
    raise ValueError("Type and term do not match in `reflect`")

def reify(generator, ty, semantic):
    if isinstance(ty, type_syntax.Arrow) and isinstance(semantic, semantics.Lambda):
        v = generator.next()
        return syntax.Lambda(v, reify(generator, ty.target, semantic.function(reflect(generator, ty.source, syntax.Var(v)))))
    if isinstance(ty, type_syntax.Product) and isinstance(semantic, semantics.Pair):
        first, second = semantic.pair
        return syntax.Pair(reify(generator, ty.first, first), reify(generator, ty.second, second))
    if isinstance(ty, type_syntax.Basic) and isinstance(semantic, semantics.Syntax):
        return semantic.syntax
    raise ValueError("Type and term do not match in `reify`")

def meaning(context, term):
    if isinstance(term, syntax.Var):
        return context[term.identifier]
    if isinstance(term, syntax.Lambda):
        def inner(s):
            new_context = context.copy()
            new_context[term.identifier] = s
            return meaning(new_context, term.body)
        return semantics.Lambda(inner)
    if isinstance(term, syntax.Apply):
        function_meaning = meaning(context, term.term1)
        if isinstance(function_meaning, semantics.Lambda):
            return function_meaning.function(meaning(context, term.term2))
        raise ValueError("Cannot apply non-function in `meaning`")
    if isinstance(term, syntax.Pair):
        return semantics.Pair(meaning(context, term.term1), meaning(context, term.term2))
    if isinstance(term, syntax.Fst):
        pair_meaning = meaning(context, term.term)
        if isinstance(pair_meaning, semantics.Pair):
            a, _ = pair_meaning.pair
            return a
        raise ValueError("Cannot take fst of non-pair in `meaning`")
    if isinstance(term, syntax.Snd):
        pair_meaning = meaning(context, term.term)
        if isinstance(pair_meaning, semantics.Pair):
            _, b = pair_meaning.pair
            return b
    raise ValueError("Invalid syntax in `meaning`")
