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

    def test_two_empty_words_have_correct_distance(self):
        self.assertEqual(self.dl.edit_distance("", ""), 0)

    def test_transposition_gives_correct_distance(self):
        self.assertEqual(self.dl.edit_distance("rapsi", "raspi"), 1)

    def test_typo_edit_distance_with_adjacent_keys(self):
        self.assertEqual(self.dl.edit_distance("joira", "koira"), 0.25)

    def test_long_strings(self):
        long_string1 = "a" * 1000
        long_string2 = "a" * 999 + "b"
        self.assertEqual(self.dl.edit_distance(long_string1, long_string2), 1)

    def test_special_characters(self):
        self.assertEqual(self.dl.edit_distance("hello!", "hello?"), 1)

    def test_case_sensitivity(self):
        self.assertEqual(self.dl.edit_distance("Hello", "hello"), 1)

    @given(st.text(), st.text())
    @settings(max_examples=100)
    def test_random_strings(self, s1, s2):
        self.assertGreaterEqual(self.dl.edit_distance(s1, s2), 0)

    @given(value=st.text(min_size=1, max_size=500))
    @settings(max_examples=1000)
    def test_right_distance_hypothesis(self, value):
        for i in self.words:
            word = self.dl.edit_distance(value, i)
            self.assertGreaterEqual(word, 0)

    @given(
        value=st.text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=1,
            max_size=100,
        )
    )
    def test_right_distance_with_same_word_hypothesis(self, value):
        self.assertEqual(self.dl.edit_distance(value, value), 0)

    @given(
        value=st.text(
            alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
            min_size=1,
            max_size=500,
        )
    )
    @settings(max_examples=1000)
    def test_distance_to_empty_word_is_correct_hypothesis(self, value):
        string = ""
        self.assertEqual(self.dl.edit_distance(string, value), len(value))
