from pathlib import Path
from services.trie import Trie
from services.dameraulevenshtein import DamerauLevenshtein

ROOT_DIR = Path(__file__).parent
TEXT_FILE = ROOT_DIR / "words.txt"


class StringService:
    """Luokka, joka käsittelee käyttöliittymän syötteitä, lisää ja hakee sanoja trie-tietorakenteesta sekä vertaa sanoja/lauseita Damerau-Levenshtein -etäisyyden avulla.

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
        self.sentence = []
        self.close_word = ""

    def add_file_words_to_trie(self):
        """Lisää words.txt -tiedoston sanat trie-tietorakenteeseen.

        Raises:
            FileNotFoundError: Jos words.txt-tiedostoa ei löydy.
        """

        with open(TEXT_FILE, encoding="utf-8") as words_file:
            for word in words_file:
                word = word.strip()
                self.trie.add_word(word)

    def search_word_from_trie(self, word):
        """Hakee käyttäjän antamaa sanaa trie-tietorakenteesta.

        Jos syöte on yksittäinen sana, tarkistaa sanan olemassaolon
        tai etsii lähimmän vastaavuuden. Jos syöte on lause, vertailee
        sanoja erikseen.

        Args:
            word: Käyttäjän antama syöte.

        Returns:
            bool: True, jos yksittäinen sana löytyy, muuten False.
        """

        if self.trie.search_word(word):
            return True
        sentence = word.split()
        if len(sentence) == 1:
            return self.compare_word_with_dl(word)
        return self.compare_sentence_with_dl(sentence)

    def compare_word_with_dl(self, word):
        """Vertaa annetua sanaa trie-tietorakenteen sanoihin Damerau Levenshtein -etäisyyden avulla.

        Etsii trie-tietorakenteesta lähimmän sanan, jonka etäisyys on
        korkeintaan 1, ja tallentaa sen muuttujaan `close_word`.

        Args:
            word (str): Käyttäjän antama sana.

        Returns:
            bool: False, jolloin käyttöliittymä voi antaa sanalle korjausehdotuksen.
        """

        self.close_word = ""
        minimum_distance = float('inf')
        for compare_word in self.trie.get_all_words():
            if abs(len(word) - len(compare_word)) <= 1:
                comparison = self.dl.edit_distance(word, compare_word)
                if comparison < minimum_distance:
                    minimum_distance = comparison
                    self.close_word = compare_word
        return False

    def compare_sentence_with_dl(self, sentence):
        """Vertaa annettun lauseen sanoja trie-tietorakenteeseen. 

        Etsii jokaisen sanan trie-tietorakenteesta tai lähimmän vastineen
        Damerau-Levenshtein -etäisyyden perusteella. Korjausehdotukset
        lisätään `sentence`-listaan.

        Args:
            sentence (list): Käyttäjän antama lause.

        Returns:
            bool: True, jos koko lause on oikein. False, jolloin käyttöliittymä voi antaa lauseelle korjausehdotuksen.
        """

        self.sentence = []
        for word in sentence:
            if self.trie.search_word(word):
                self.sentence.append(word)
            else:
                self.compare_word_with_dl(word)
                self.sentence.append(self.close_word)
                self.close_word = ""
                
        if self.sentence == sentence:
            return True

        return False

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

    def __str__(self):
        """Muodostaa merkkijonomuotoisen esityksen riippuen sanan tai lauseen korjauksista.

        Jos sana tai lause löytyi trie-tietorakenteesta, palauttaa sitä
        vastaavan korjausehdotuksen. Muuten ilmoittaa, että syötettä ei löytynyt.

        Returns:
            str: Korjausehdotus tai löytyikö sana/lause vai ei.
        """
        if len(self.close_word) > 0:
            return f"Tarkoititko: '{self.close_word}'?"
        if len(self.sentence) > 0:
            return f"Tarkoititko: '{' '.join(self.sentence)}'?"
        return "Sanaa tai lausetta ei löytynyt"


string_service = StringService()
