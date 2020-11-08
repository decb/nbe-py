from nbe.syntax import *
from nbe.type_syntax import *


def parse_syntax(string):
    return to_syntax(to_tree(tokenise(string)))


def parse_type_syntax(string):
    return to_type_syntax(to_tree(tokenise(string)))


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


def to_syntax(tree):
    if isinstance(tree, str):
        return Var(tree)
    first = tree[0]
    if first == "fst":
        if len(tree) == 2:
            return Fst(to_syntax(tree[1]))
        raise SyntaxError("Expected 1 argument to `fst`")
    if first == "snd":
        if len(tree) == 2:
            return Snd(to_syntax(tree[1]))
        raise SyntaxError("Expected 1 argument to `snd`")
    if first == "pair":
        if len(tree) == 3:
            return Pair(to_syntax(tree[1]), to_syntax(tree[2]))
        raise SyntaxError("Expected 2 arguments to `pair`")
    if first == "lambda":
        if len(tree) == 3 and isinstance(tree[1], str):
            return Lambda(tree[1], to_syntax(tree[2]))
        raise SyntaxError("Expected variable name and body for `lambda`")
    if len(tree) == 2:
        return Apply(to_syntax(tree[0]), to_syntax(tree[1]))
    raise SyntaxError("Cannot parse expression")


def to_type_syntax(tree):
    if isinstance(tree, str):
        return Basic(tree)
    first = tree[0]
    if first == "->":
        if len(tree) == 3:
            return Arrow(to_type_syntax(tree[1]), to_type_syntax(tree[2]))
        raise SyntaxError("Expected 2 arguments to `->`")
    if first == "*":
        if len(tree) == 3:
            return Product(to_type_syntax(tree[1]), to_type_syntax(tree[2]))
        raise SyntaxError("Expected 2 arguments to `*`")
    raise SyntaxError("Cannot parse type")
