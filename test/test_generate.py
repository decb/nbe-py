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

    def test_currying(self):
        term = generate(parse_type_syntax(
            "(-> (-> (* a b) c) (-> a (-> b c)))"))
        self.assertEqual(
            str(term),
            "(lambda a (lambda b (lambda c (a (pair b c)))))")

    def test_product_associativity(self):
        term = generate(parse_type_syntax("(-> (* a (* b c)) (* (* a b) c))"))
        self.assertEqual(
            str(term),
            "(lambda a (pair (pair (fst a) (fst (snd a))) (snd (snd a))))")

    def test_composition(self):
        term = generate(parse_type_syntax(
            "(-> (-> a b) (-> (-> b c) (-> a c)))"))
        self.assertEqual(
            str(term),
            "(lambda a (lambda b (lambda c (b (a c)))))")
