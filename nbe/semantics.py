class Lambda:
    def __init__(self, f):
        this._f = f

    @property
    def f(self):
        return this._f


class Pair:
    def __init__(self, pair):
        this._pair = pair

    @property
    def pair(self):
        return this._pair


class Syntax:
    def __init__(self, syntax):
        this._syntax = syntax

    @property
    def syntax(self):
        return this._syntax
