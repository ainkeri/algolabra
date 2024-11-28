import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from services.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add_word("koira")
        self.trie.add_word("koru")
        self.trie.add_word("kissa")
        self.trie.add_word("kiloinen")
        self.trie.add_word("aura")
        self.trie.add_word("aurajuusto")
        self.trie.add_word("auringoton")
        self.trie.add_word("patonki")
        self.trie.add_word("parta")

    def test_str_is_returned_correctly_with_pre_order_traversal(self):
        self.trie.check_correct_structure()
        correct_string = ", k, o, i, r, a, r, u, i, s, s, a, l, o, i, n, e, n, a, u, r, a, j, u, u, s, t, o, i, n, g, o, t, o, n, p, a, t, o, n, k, i, r, t, a"
        self.assertEqual(self.trie.__str__(), correct_string)

    def test_search_word(self):
        self.assertTrue(self.trie.search_word("koira"))
        self.assertFalse(self.trie.search_word("nothere"))

    @given(arvo=st.text(min_size=1, max_size=500))
    @settings(max_examples=500)
    def test_adding_to_trie_hypothesis(self, arvo):
        self.trie.add_word(arvo)
        self.assertTrue(self.trie.search_word(arvo))
