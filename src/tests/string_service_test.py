import unittest
from services.string_service import StringService


class TestStringService(unittest.TestCase):
    def setUp(self):
        self.string_service = StringService()
        self.string_service.add_file_words_to_trie()

    def test_word_in_trie_is_found(self):
        self.assertEqual(self.string_service.word_exists_in_trie("koira"), True)

    def test_word_not_in_trie_is_not_found(self):
        self.assertEqual(self.string_service.word_exists_in_trie("nakkikiska"), False)

    def test_valid_string_can_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string("newstring"), True)

    def test_not_valid_string_can_not_be_added_to_trie(self):
        self.assertEqual(self.string_service.create_string(""), False)

    def test_word_is_corrected(self):
        string = "sirsi"

        self.assertEqual(self.string_service.returns_closest_list(string), ["sitsi"])

    def test_sentence_is_corrected(self):
        sentence = "koira ruu kisra lapio"

        self.assertEqual(
            self.string_service.returns_closest_list(sentence),
            ["koira", "tiu", "kusta", "lapio"],
        )

    def test_word_too_complex_is_corrected(self):
        string = "slkdjskldjksjd"

        self.assertEqual(
            self.string_service.returns_closest_list(string), ["salamanleimaus"]
        )
