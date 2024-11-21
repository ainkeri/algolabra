import unittest
from services.string_service import StringService


class TestStringService(unittest.TestCase):
    def setUp(self):
        self.string_service = StringService()
        self.string_service.add_file_words_to_trie()

    def test_word_in_trie_is_found(self):
        self.assertEqual(
            self.string_service.search_word_from_trie("koira"), True)

    def test_valid_string_can_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string("newstring"), True)

    def test_not_valid_string_can_not_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string(""), False)

    def test_word_not_in_trie_gets_suggestion(self):
        string = "sirsi"

        self.string_service.search_word_from_trie(string)

        self.assertEqual(self.string_service.__str__(), "Tarkoititko: 'hirsi'?")
        self.assertFalse(False)

    def test_word_too_complex_gets_no_suggestion(self):
        string = "slkdjskldjksjd"

        self.string_service.search_word_from_trie(string)

        self.assertEqual(self.string_service.__str__(), "Sanaa tai lausetta ei löytynyt")
        self.assertFalse(False)
