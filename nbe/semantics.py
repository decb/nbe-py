class Lambda:
    def __init__(self, function):
        self._function = function

    @property
    def function(self):
        return self._function


class Pair:
    def __init__(self, pair):
        self._pair = pair

    @property
    def pair(self):
        return self._pair


class Syntax:
    def __init__(self, syntax):
        self._syntax = syntax

    @property
    def syntax(self):
        return self._syntax
