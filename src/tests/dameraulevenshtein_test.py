import unittest
from services.dameraulevenshtein import DamerauLevenshtein

class TestDamerauLevenshtein(unittest.TestCase):
    def setUp(self):
        self.dl = DamerauLevenshtein()
        self.word1 = "lapoi"
        self.word2 = "lapsi"
    
    def test_words_compared_have_distance_one(self):
        self.assertEqual(self.dl.edit_distance(self.word1, self.word2), 1)
    
    def test_words_compared_have_distance_two(self):
        self.assertEqual(self.dl.edit_distance(self.word1, "lapua"), 2)
    
    def test_words_compared_have_distance_two_again(self):
        self.assertEqual(self.dl.edit_distance(self.word2, "lapua"), 2)

    def test_words_compared_have_distance_three(self):
        self.assertEqual(self.dl.edit_distance(self.word2, "virsi"), 3)
    
    def test_words_given_have_correct_distance(self):
        self.assertEqual(self.dl.edit_distance("viri", "virsi"), 1)
    
    def test_one_empty_word_has_right_distance(self):
        self.assertEqual(self.dl.edit_distance(self.word1, ""), 5)
    
    def test_one_empty_word_has_right_distance_again(self):
        self.assertEqual(self.dl.edit_distance("", self.word2), 5)
    
    def test_two_empty_words_has_right_distance(self):
        self.assertEqual(self.dl.edit_distance("", ""), 0)