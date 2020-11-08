import syntax


def print_expression(expression):
    if isinstance(expression, syntax.Var):
        return expression.identifier
    if isinstance(expression, syntax.Lambda):
        return f"(lambda {expression.identifier} {print_expression(expression.body)})"
    if isinstance(expression, syntax.Apply):
        return f"({print_expression(expression.term1)} {print_expression(expression.term2)})"
    if isinstance(expression, syntax.Pair):
        return f"(pair {print_expression(expression.term1)} {print_expression(expression.term2)})"
    if isinstance(expression, syntax.Fst):
        return f"(fst {print_expression(expression.term)})"
    if isinstance(expression, syntax.Snd):
        return f"(snd {print_expression(expression.term)})"
    raise ValueError("Invalid syntax in printer")
