import unittest
from services.string_service import StringService


class TestStringService(unittest.TestCase):
    def setUp(self):
        self.string_service = StringService()
        self.string_service.add_file_words_to_trie()

    def test_word_in_trie_is_found(self):
        self.assertEqual(self.string_service.search_word_from_trie("koira"), True)

    def test_valid_string_can_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string("newstring"), True)

    def test_not_valid_string_can_not_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string(""), False)

    def test_word_not_in_trie_gets_suggestion(self):
        string = "sirsi"

        self.string_service.search_word_from_trie(string)

        self.assertEqual(str(self.string_service), "Tarkoititko: 'hirsi'?")

    def test_sentence_gets_a_suggestion(self):
        sentence = "koira ruu kisra lapio"

        self.string_service.search_word_from_trie(sentence)

        self.assertEqual(
            str(self.string_service), "Tarkoititko: 'koira juu kisa lapio'?"
        )

    def test_correct_sentence_is_found(self):
        sentence = "koira lapsi kissa lapio hiekka"

        self.string_service.search_word_from_trie(sentence)

    def test_word_too_complex_gets_suggestion(self):
        string = "slkdjskldjksjd"

        self.string_service.search_word_from_trie(string)

        self.assertEqual(str(self.string_service), "Tarkoititko: 'oikaisulukija'?")

    def test_word_or_sentence_not_found(self):
        self.assertEqual(str(self.string_service), "Sanaa tai lausetta ei löytynyt")
