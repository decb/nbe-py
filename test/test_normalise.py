import unittest
from nbe.parser import parse, parse_type
from nbe.normalise import normalise

S = "(lambda a (lambda b (lambda c ((a c) (b c)))))"
K = "(lambda a (lambda b a))"
SKK = f"(({S} {K}) {K})"


class TestNBE(unittest.TestCase):
    def test_skk(self):
        term = parse(SKK)
        a_to_a = parse_type("(-> a a)")
        normal_form = normalise(a_to_a, term)
        self.assertEqual(str(normal_form), "(lambda a a)")

    def test_eta_long(self):
        term = parse(SKK)
        a_to_b_squared = parse_type("(-> (-> a b) (-> a b))")
        normal_form = normalise(a_to_b_squared, term)
        self.assertEqual(str(normal_form), "(lambda a (lambda b (a b)))")

    def test_swap(self):
        term = parse(
            f"((lambda x (pair (snd x) (fst x))) (pair (lambda x x) {K}))")
        swap_type = parse_type("(* (-> a (-> b a)) (-> a a))")
        normal_form = normalise(swap_type, term)
        self.assertEqual(
            str(normal_form),
            "(pair (lambda a (lambda b a)) (lambda c c))")
