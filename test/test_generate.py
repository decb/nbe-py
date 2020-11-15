import unittest
from nbe.parser import parse_type_syntax
from nbe.generate import generate


class TestGeneration(unittest.TestCase):
    def test_i(self):
        term = generate(parse_type_syntax("(-> a a)"))
        self.assertEqual(str(term), "(lambda a a)")

    def test_s(self):
        term = generate(parse_type_syntax(
            "(-> (-> a (-> b c)) (-> (-> a b) (-> a c)))"))
        self.assertEqual(
            str(term),
            "(lambda a (lambda b (lambda c ((a c) (b c)))))")

    def test_swap(self):
        term = generate(parse_type_syntax("(-> (* a b) (* b a))"))
        self.assertEqual(str(term), "(lambda a (pair (snd a) (fst a)))")
