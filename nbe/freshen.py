from nbe.syntax import *


def freshen(term, generator, context={}):
    if isinstance(term, Var):
        return Var(context[term.identifier])
    if isinstance(term, Lambda):
        new_identifier = generator.next()
        context[term.identifier] = new_identifier
        return Lambda(new_identifier, freshen(term.body, generator, context))
    if isinstance(term, Apply):
        return Apply(
            freshen(
                term.term1, generator, context), freshen(
                term.term2, generator, context))
    if isinstance(term, Pair):
        return Pair(
            freshen(
                term.term1, generator, context), freshen(
                term.term2, generator, context))
    if isinstance(term, Fst):
        return Fst(freshen(term.term, generator, context))
    if isinstance(term, Snd):
        return Snd(freshen(term.term, generator, context))
    raise ValueError("Invalid syntax in `freshen`")
