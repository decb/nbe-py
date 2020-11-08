import syntax


def parse(string):
    return to_ast(to_tree(tokenise(string)))


def tokenise(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()


def to_tree(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Expected more input")
    token = tokens.pop(0)
    if token == '(':
        body = []
        while tokens[0] != ')':
            body.append(to_tree(tokens))
        tokens.pop(0)
        return body
    if token == ')':
        raise SyntaxError("Unexpected ')'")
    return token


def to_ast(tree):
    if isinstance(tree, str):
        return syntax.Var(str)
    first = tree[0]
    if first == "fst":
        if len(tree) == 2:
            return syntax.Fst(to_ast(tree[1]))
        raise SyntaxError("Expected 1 argument to `fst`")
    if first == "snd":
        if len(tree) == 2:
            return syntax.Snd(to_ast(tree[1]))
        raise SyntaxError("Expected 1 argument to `snd`")
    if first == "pair":
        if len(tree) == 3:
            return syntax.Pair(to_ast(tree[1]), to_ast(tree[2]))
        raise SyntaxError("Expected 2 arguments to `pair`")
    if first == "lambda":
        if len(tree) == 3 and isinstance(tree[1], str):
            return syntax.Lambda(tree[1], to_ast(tree[2]))
        raise SyntaxError("Expected variable name and body for `lambda`")
    if len(tree) == 2:
        return syntax.Apply(to_ast(tree[1]), to_ast(tree[2]))
    raise SyntaxError("Cannot parse expression")
