from pathlib import Path
from services.trie import Trie
from services.dameraulevenshtein import DamerauLevenshtein

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "words.txt"


class StringService:
    """Luokka, joka käsittelee käyttöliittymän syötteitä, lisää ja hakee sanoja
       trie-tietorakenteesta sekä vertaa sanoja/lauseita Damerau-Levenshtein -etäisyyden avulla.

    Attributes:
        trie (Trie):
            Trie-luokan ilmentymä, jota käytetään sanojen tallentamiseen ja hallintaan.
        dl (DamerauLevenshtein):
            DamerauLevenshtein-luokan ilmentymä, jota käytetään sanojen vertaamiseen keskenään.
        sentence (list):
            Lista lauseen sanoista, joita verrataan trie-tietorakenteeseen.
        close_word (str):
            Viimeisin lähellä oleva sana, joka löytyy trie-tietorakenteesta.
    """

    def __init__(self):
        """Luokan konstruktori.

        Alustaa trie- ja Damerau-Levenshtein -tietorakenteet sekä tyhjät muuttujat
        lauseen sanojen ja lähimmän sanan tallentamiselle.
        """

        self.trie = Trie()
        self.dl = DamerauLevenshtein()

    def add_file_words_to_trie(self):
        """Lisää words.txt -tiedoston sanat trie-tietorakenteeseen.

        Raises:
            FileNotFoundError: Jos words.txt-tiedostoa ei löydy.
        """

        with open(TEXT_FILE, encoding="utf-8") as words_file:
            for word in words_file:
                word = word.strip()
                self.trie.add_word(word)

    def word_exists_in_trie(self, word):
        if self.trie.search_word(word):
            return True
        return False

    def returns_closest_list(self, phrase):
        phrase = phrase.split()
        corrected_phrase = []

        for word in phrase:
            if self.trie.search_word(word):
                corrected_phrase.append(word)
            else:
                corrected_phrase.append(self.compare_words(word))

        return corrected_phrase

    def compare_words(self, word):
        """Vertaa annetua sanaa trie-tietorakenteen sanoihin Damerau Levenshtein -etäisyyden avulla.

        Etsii trie-tietorakenteesta lähimmän sanan, jonka etäisyys on
        pienin (pienin etäisyys tallennettu minimum_distance -muuttujaan),
        ja tallentaa sanan muuttujaan `closest_word`.

        Args:
            word (str): Käyttäjän antama sana.

        Returns:
            string: sanan, jolla on lyhin etäisyys annettuun sanaan.
        """

        closest_word = ""
        minimum_distance = float("inf")
        for compare_word in self.trie.get_all_words():
            if abs(len(word) - len(compare_word)) <= 1:
                comparison = self.dl.edit_distance(word, compare_word)
                if comparison < minimum_distance:
                    minimum_distance = comparison
                    closest_word = compare_word
        return closest_word

    def create_string(self, string):
        """Lisää annetun sanan trie-tietorakenteeseen.

        Tyhjää merkkijonoa ei lisätä.

        Args:
            string (str): Käyttäjän syöte.

        Returns:
            bool: True, jos sana lisättiin onnistuneesti, muuten False.
        """

        string = string.strip()
        if len(string) > 0:
            self.trie.add_word(string)
            return True
        return False


string_service = StringService()
