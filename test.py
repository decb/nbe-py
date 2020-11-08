import unittest
from nbe.parser import parse_syntax, parse_type_syntax
from nbe.normalise import nbe
from nbe.printer import print_syntax

S = "(lambda x (lambda y (lambda z ((x z) (y z)))))"
K = "(lambda x (lambda y x))"
SKK = f"(({S} {K}) {K})"


class TestNBE(unittest.TestCase):
    def test_skk(self):
        term = parse_syntax(SKK)
        a_to_a = parse_type_syntax("(-> a a)")
        normal_form = nbe(a_to_a, term)
        result = print_syntax(normal_form)
        self.assertEqual(result, "(lambda a a)")

    def test_eta_long(self):
        term = parse_syntax(SKK)
        a_to_b_squared = parse_type_syntax("(-> (-> a b) (-> a b))")
        normal_form = nbe(a_to_b_squared, term)
        result = print_syntax(normal_form)
        self.assertEqual(result, "(lambda a (lambda b (a b)))")

    def test_swap(self):
        term = parse_syntax(
            f"((lambda x (pair (snd x) (fst x))) (pair (lambda x x) {K}))")
        swap_type = parse_type_syntax("(* (-> a (-> b a)) (-> a a))")
        normal_form = nbe(swap_type, term)
        result = print_syntax(normal_form)
        self.assertEqual(result, "(pair (lambda a (lambda b a)) (lambda c c))")


if __name__ == "__main__":
    unittest.main()
