import syntax


def parse(string):
    return to_ast(structure(tokenise(string)))


def tokenise(string):
    return string.replace("(", " ( ").replace(")", " ) ").split()


def structure(tokens):
    if len(tokens) == 0:
        raise SyntaxError("Expected more input")
    token = tokens.pop(0)
    if token == '(':
        body = []
        while tokens[0] != ')':
            body.append(structure(tokens))
        tokens.pop(0)
        return body
    elif token == ')':
        raise SyntaxError("Unexpected ')'")
    else:
        return token


def to_ast(structure):
    if isinstance(structure, str):
        return syntax.Var(str)
    first = structure[0]
    if first == "fst":
        if len(structure) == 2:
            return syntax.Fst(to_ast(structure[1]))
        else:
            raise SyntaxError("Expected 1 argument to `fst`")
    elif first == "snd":
        if len(structure) == 2:
            return syntax.Snd(to_ast(structure[1]))
        else:
            raise SyntaxError("Expected 1 argument to `snd`")
    elif first == "pair":
        if len(structure) == 3:
            return syntax.Pair(to_ast(structure[1]), to_ast(structure[2]))
        else:
            raise SyntaxError("Expected 2 arguments to `pair`")
    elif first == "lambda":
        if len(structure) == 3 and isinstance(structure[1], str):
            return syntax.Lambda(structure[1], to_ast(structure[2]))
        else:
            raise SyntaxError("Expected variable name and body for `lambda`")
    elif len(structure) == 2:
        return syntax.Apply(to_ast(structure[1]), to_ast(structure[2]))
    else:
        raise SyntaxError("Cannot parse expression")
