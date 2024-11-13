import unittest
from services.dameraulevenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()
        self.word = "lapoi"

    def test_words_compared_have_distance_one(self):
        self.assertEqual(self.dl.edit_distance(self.word, "lapsi"), 1)

    def test_words_compared_have_distance_two(self):
        self.assertEqual(self.dl.edit_distance(self.word, "lapua"), 2)

    def test_words_compared_have_distance_three(self):
        self.assertEqual(self.dl.edit_distance(self.word, "varsi"), 3)

    def test_words_compared_have_greater_edit_distance(self):
        self.assertEqual(self.dl.edit_distance(
            "oikeudenmukaisuus", "virsi"), 15)

    def test_one_empty_word_has_right_distance(self):
        self.assertEqual(self.dl.edit_distance(self.word, ""), 5)

    def test_two_empty_words_has_right_distance(self):
        self.assertEqual(self.dl.edit_distance("", ""), 0)
