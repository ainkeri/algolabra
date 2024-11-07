import unittest
from services.trie import Trie

class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_a_word_is_added_to_trie_and_found(self):
        word = "testword"
        self.trie.add_word(word)

        self.assertEqual(self.trie.search_word(word), True)

    def test_a_word_not_in_trie_is_not_found(self):
        word = "notintrie"

        self.assertEqual(self.trie.search_word(word), False)