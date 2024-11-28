import unittest
from services.trie import TrieNode


class TestTrieNode(unittest.TestCase):
    def setUp(self):
        self.root = TrieNode("")

    def test_trienode_is_created(self):
        self.assertIsInstance(self.root, TrieNode)
