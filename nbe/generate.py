from nbe.freshen import *
from nbe.syntax import *
from nbe.type_syntax import *
from nbe.name_generator import NameGenerator


def generate(tau):
    result = reduce_right(tau, NameGenerator(), [])
    return freshen(result, NameGenerator())


def reduce_right(tau, generator, context):
    if isinstance(tau, Arrow):
        identifier = generator.next()
        new_context = context.copy()
        new_context.append((Var(identifier), tau.source))
        return Lambda(
            identifier,
            reduce_right(
                tau.target,
                generator,
                new_context))
    if isinstance(tau, Product):
        first = reduce_right(tau.first, generator, context)
        second = reduce_right(tau.second, generator, context)
        return Pair(first, second)
    if isinstance(tau, Basic):
        return reduce_left(tau, generator, context)
    raise TypeError("Unknown type in `reduce_right`")


def reduce_left(tau, generator, context):
    candidates = [i for i, t in context if t == tau]
    if len(candidates) > 0:
        return candidates[0]
    if len([p for _, p in context if not isinstance(p, Basic)]) == 0:
        raise TypeError("Cannot find type in context")
    first, rest = context[0], context[1:]
    if isinstance(first[1], Arrow):
        try:
            argument = reduce_right(first[1].source, generator, rest)
            rest.append((Apply(first[0], argument), first[1].target))
        finally:
            return reduce_left(tau, generator, rest)
    if isinstance(first[1], Product):
        rest.append((Fst(first[0]), first[1].first))
        rest.append((Snd(first[0]), first[1].second))
        return reduce_left(tau, generator, rest)
    if isinstance(first[1], Basic):
        rest.append(first)
        return reduce_left(tau, generator, rest)
    raise TypeError("Unknown type in `reduce_left`")
