from pathlib import Path
from services.trie import Trie
from services.dameraulevenshtein import DamerauLevenshtein

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
        self.sentence = []
        self.close_word = ""

    def add_file_words_to_trie(self):
        with open(TEXT_FILE, encoding="utf-8") as words_file:
            for word in words_file:
                word = word.strip()
                self.trie.add_word(word)

    def search_word_from_trie(self, word):
        if self.trie.search_word(word):
            return True
        sentence = word.split()
        if len(sentence) == 1:
            return self.compare_word_with_dl(word)
        return self.compare_sentence_with_dl(sentence)

    def compare_word_with_dl(self, word):
        self.close_word = ""
        for compare_word in self.trie.get_all_words():
            if abs(len(word) - len(compare_word)) <= 1:
                comparison = self.dl.edit_distance(word, compare_word)
                if comparison <= 1:
                    self.close_word = compare_word
                    return False
        return False
    
    def compare_sentence_with_dl(self, sentence):
        self.sentence = []
        for word in sentence:
            if self.trie.search_word(word):
                self.sentence.append(word)
            else:
                self.compare_word_with_dl(word)
                if len(self.close_word) > 0:
                    self.sentence.append(self.close_word)
                    self.close_word = ""
        return False

    def create_string(self, string):
        string = string.strip()
        if len(string) > 0:
            self.trie.add_word(string)
            return True
        return False

    def __str__(self):
        if len(self.close_word) > 0:
            return f"Tarkoititko: '{self.close_word}'?"
        if len(self.sentence) > 0:
            return f"Tarkoititko: '{' '.join(self.sentence)}'?"
        return "Sanaa ei löytynyt"


string_service = StringService()
