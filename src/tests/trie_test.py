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
    
    def test_str_is_returned_correctly_with_dfs(self):
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

        self.trie.get_all_words()

        self.assertEqual(self.trie.__str__(), "metsänomistaja, metsänomistus, metsänparannus, musiikkinäytelmä, musiikkiopinnot, musiikkiopisto, normaaliolot, normaaliobjektiivi, normaalipaino, normaalinäköinen")
    
    def test_get_all_words(self):
        self.trie.add_word("miuku")
        self.trie.add_word("mauku")

        all_words = self.trie.get_all_words()

        self.assertEqual(all_words, ["miuku", "mauku"])
    
    

        


