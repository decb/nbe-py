class Var:
    def __init__(self, identifier):
        self._identifier = identifier

    @property
    def identifier(self):
        return self._identifier


class Lambda:
    def __init__(self, identifier, body):
        self._identifier, self._body = identifier, body

    @property
    def identifier(self):
        return self._identifier

    @property
    def body(self):
        return self._body


class Apply:
    def __init__(self, term1, term2):
        self._term1, self._term2 = term1, term2

    @property
    def term1(self):
        return self._term1

    @property
    def term2(self):
        return self._term2


class Pair:
    def __init__(self, term1, term2):
        self._term1, self._term2 = term1, term2

    @property
    def term1(self):
        return self._term1

    @property
    def term2(self):
        return self._term2


class Fst:
    def __init__(self, term):
        self._term = term

    @property
    def term(self):
        return self._term


class Snd:
    def __init__(self, term):
        self._term = term

    @property
    def term(self):
        return self._term
