from services.trie import Trie
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
        
    def add_file_words_to_trie(self):
        with open(TEXT_FILE) as words_file:
            for word in words_file:
                word = word.strip()
                self.trie.add_word(word)
    
    def search_word_from_trie(self, word):
        if self.trie.search_word(word):
            return True
        else:
            return False
    
    def create_string(self, string):
        string = string.strip()
        if len(string) > 0:
            self.trie.add_word(string)
        return False

string_service = StringService()
    