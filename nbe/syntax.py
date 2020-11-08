class Var:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id


class Lambda:
    def __init__(self, id, body):
        this._id, this._body = id, body

    @property
    def id(self):
        return self._id

    @property
    def body(self):
        return self._body


class Apply:
    def __init__(self, term1, term2):
        this._term1, this._term2 = term1, term2

    @property
    def term1(self):
        return self._term1

    @property
    def term2(self):
        return self._term2


class Pair:
    def __init__(self, term1, term2):
        this._term1, this._term2 = term1, term2

    @property
    def term1(self):
        return self._term1

    @property
    def term2(self):
        return self._term2


class Fst:
    def __init__(self, term):
        this._term = term

    @property
    def term(self):
        return self._term


class Snd:
    def __init__(self, term):
        this._term = term

    @property
    def term(self):
        return self._term
