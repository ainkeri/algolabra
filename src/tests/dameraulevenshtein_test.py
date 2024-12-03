import unittest
from hypothesis import given, settings
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
        self.assertEqual(self.dl.edit_distance("oikeudenmukaisuus", "virsi"), 14.25)

    def test_compared_word_is_empty_string(self):
        self.assertEqual(self.dl.edit_distance(self.word, ""), 5)

    def test_user_input_is_empty_string(self):
        self.assertEqual(self.dl.edit_distance("", self.word), 5)

    def test_two_empty_words_has_right_distance(self):
        self.assertEqual(self.dl.edit_distance("", ""), 0)

    def test_transposition_gives_correct_distance(self):
        self.assertEqual(self.dl.edit_distance("rapsi", "raspi"), 1)

    def test_typo_edit_distance_with_adjacent_keys(self):
        self.assertEqual(self.dl.edit_distance("joira", "koira"), 0.25)

    @given(arvo=st.text(min_size=1, max_size=500))
    @settings(max_examples=1000)
    def test_right_distance_hypothesis(self, arvo):
        for i in self.words:
            word = self.dl.edit_distance(arvo, i)
            self.assertGreaterEqual(word, 0)

    @given(
        arvo=st.text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=1,
            max_size=100,
        )
    )
    def test_right_distance_with_same_word_hypothesis(self, arvo):
        self.assertEqual(self.dl.edit_distance(arvo, arvo), 0)
