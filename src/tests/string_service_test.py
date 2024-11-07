import unittest
from services.string_service import StringService

class TestStringService(unittest.TestCase):
    def setUp(self):
        self.string_service = StringService()
        self.string_service.add_file_words_to_trie()
    
    def test_word_in_trie_is_found(self):
        self.assertEqual(self.string_service.search_word_from_trie("koira"), True)
    
    def test_word_not_in_trie_is_not_found(self):
        self.assertEqual(self.string_service.search_word_from_trie("jdleajhdle"), False)

    def test_valid_string_can_be_added_to_trie(self):
        string = "newstring"

        self.string_service.create_string(string)

        self.assertEqual(self.string_service.search_word_from_trie(string), True)
    
    def test_not_valid_string_can_not_be_added_to_trie(self):
        string = ""

        self.string_service.create_string(string)

        self.assertEqual(self.string_service.search_word_from_trie(string), False)