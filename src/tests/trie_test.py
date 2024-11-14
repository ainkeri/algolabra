import unittest
from hypothesis import given, settings
import hypothesis.strategies as st
from services.trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()
        self.trie.add_word("metsänomistaja")
        self.trie.add_word("normaaliolot")
        self.trie.add_word("musiikkinäytelmä")
        self.trie.add_word("musiikkiopinnot")
        self.trie.add_word("normaalipaino")
        self.trie.add_word("metsänomistus")
        self.trie.add_word("normaaliobjektiivi")
        self.trie.add_word("musiikkiopisto")
        self.trie.add_word("metsänparannus")
        self.trie.add_word("normaalinäköinen")

    def test_str_is_returned_correctly_with_dfs(self):
        self.trie.get_all_words()

        self.assertEqual(self.trie.__str__(
        ), "metsänomistaja, metsänomistus, metsänparannus, musiikkinäytelmä, musiikkiopinnot, musiikkiopisto, normaaliolot, normaaliobjektiivi, normaalipaino, normaalinäköinen")

    def test_search_word(self):
        self.assertTrue(self.trie.search_word("normaaliolot"))
        self.assertFalse(self.trie.search_word("nothere"))

    @given(arvo=st.text(min_size=1, max_size=500))
    @settings(max_examples=500)
    def test_adding_to_trie_hypothesis(self, arvo):
        self.trie.add_word(arvo)
        self.assertTrue(self.trie.search_word(arvo))
