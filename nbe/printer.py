from nbe.syntax import *


def print_expression(expression):
    if isinstance(expression, Var):
        return expression.identifier
    if isinstance(expression, Lambda):
        return f"(lambda {expression.identifier} {print_expression(expression.body)})"
    if isinstance(expression, Apply):
        return f"({print_expression(expression.term1)} {print_expression(expression.term2)})"
    if isinstance(expression, Pair):
        return f"(pair {print_expression(expression.term1)} {print_expression(expression.term2)})"
    if isinstance(expression, Fst):
        return f"(fst {print_expression(expression.term)})"
    if isinstance(expression, Snd):
        return f"(snd {print_expression(expression.term)})"
    raise ValueError("Invalid syntax in `print_expression`")
