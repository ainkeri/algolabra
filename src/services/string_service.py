from services.trie import Trie
from services.dameraulevenshtein import DamerauLevenshtein
from pathlib import Path

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "words.txt"


class StringService:
    """Luokka, joka käsittelee käyttöliittymän syötteitä ja lisää sanoja trie-tietorakenteeseen.

    Attributes:
        trie (Trie): Trie-luokan ilmentymä, jota käytetään sanojen tallentamiseen ja hallintaan.
    """

    def __init__(self):
        self.trie = Trie()
        self.dl = DamerauLevenshtein()
        self.close_word = ""

    def add_file_words_to_trie(self):
        with open(TEXT_FILE) as words_file:
            for word in words_file:
                word = word.strip()
                self.trie.add_word(word)

    def search_word_from_trie(self, word):
        if self.trie.search_word(word):
            return True
        else:
            self.compare_words_with_dl(word)

    def compare_words_with_dl(self, word):
        for compare_word in self.trie.get_all_words():
            if abs(len(word) - len(compare_word)) <= 1:
                comparison = self.dl.edit_distance(word, compare_word)
                if comparison <= 1:
                    self.close_word = compare_word
                else:
                    return False
        return False

    def create_string(self, string):
        string = string.strip()
        if len(string) > 0:
            self.trie.add_word(string)
            return True
        return False

    def __str__(self):
        if len(self.close_word) > 0:
            return f"Did u mean: '{self.close_word}'?"
        return "Word not found"


string_service = StringService()
