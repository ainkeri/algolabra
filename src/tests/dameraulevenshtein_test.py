import unittest
from hypothesis import given, settings, example
import hypothesis.strategies as st
from services.dameraulevenshtein import DamerauLevenshtein


class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()
        self.word = "lapoi"
        self.words = ["uusi", "sana", "miu", "oikeudenmukaisuus", "kuningas", "rosvo"]

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

    @given(arvo=st.text(min_size=1, max_size=500))
    @settings(max_examples=1000)
    def test_right_distance_hypothesis(self, arvo):
        for i in self.words:
            word = self.dl.edit_distance(arvo, i)
            self.assertGreaterEqual(word, 0)
    
    @given(arvo=st.text(min_size=1, max_size=500), arvo2=st.text(min_size=1, max_size=500))
    @example("oikeudenmukaisuus", "virsi")
    def test_right_distance_between_two_hypothesis(self, arvo, arvo2):
        distance_one = self.dl.edit_distance(arvo, arvo2)
        distance_two = self.dl.edit_distance(arvo2, arvo)

        self.assertEqual(distance_one, distance_two)

    @given(arvo=st.text(min_size=1, max_size=100))
    def test_right_distance_with_same_word_hypothesis(self, arvo):
        self.assertEqual(self.dl.edit_distance(arvo, arvo), 0)