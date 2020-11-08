from nbe.syntax import *


def print_syntax(syntax):
    if isinstance(syntax, Var):
        return syntax.identifier
    if isinstance(syntax, Lambda):
        return f"(lambda {syntax.identifier} {print_syntax(syntax.body)})"
    if isinstance(syntax, Apply):
        return f"({print_syntax(syntax.term1)} {print_syntax(syntax.term2)})"
    if isinstance(syntax, Pair):
        return f"(pair {print_syntax(syntax.term1)} {print_syntax(syntax.term2)})"
    if isinstance(syntax, Fst):
        return f"(fst {print_syntax(syntax.term)})"
    if isinstance(syntax, Snd):
        return f"(snd {print_syntax(syntax.term)})"
    raise ValueError("Invalid syntax in `print_syntax`")
