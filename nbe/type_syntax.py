class Basic:
    def __init__(self, identifier):
        self._identifier = identifier

    def __eq__(self, other):
        return isinstance(other, Basic) and self.identifier == other.identifier

    def __str__(self):
        return self.identifier

    @property
    def identifier(self):
        return self._identifier


class Arrow:
    def __init__(self, source, target):
        self._source = source
        self._target = target

    def __eq__(self, other):
        return isinstance(
            other, Arrow) and self.source == other.source and self.target == other.target

    def __str__(self):
        return f"(-> {str(self.source)} {str(self.target)})"

    @property
    def source(self):
        return self._source

    @property
    def target(self):
        return self._target


class Product:
    def __init__(self, first, second):
        self._first = first
        self._second = second

    def __eq__(self, other):
        return isinstance(
            other, Product) and self.first == other.first and self.second == other.second

    def __str__(self):
        return f"(* {str(self.first)} {str(self.second)})"

    @property
    def first(self):
        return self._first

    @property
    def second(self):
        return self._second
