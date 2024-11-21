class TrieNode:
    """Luokka, joka edustaa yksittäistä solmua trie-tietorakenteessa.

    Args:
        value (str):
            Solmun sisältämä kirjain/merkki.
        child (dict):
            Sanakirja, joka sisältää lapsisolmut jokaiselle kirjaimelle.
        finish (bool):
            Arvo sille, onko solmun sanan päätepiste.
    """

    def __init__(self, char: str):
        self.value = char
        self.child = {}
        self.finish = False


class Trie:
    """Luokka, joka hallinnoi sanojen lisäämistä ja hakua trie-tietorakenteessa.

    Args:
        root (TrieNode):
            Trie-rakenteen juurisolmu, joka luodaan tyhjällä merkillä.
        words (list):
            Lista trie:n sanoista, joihin voidaan verrata käyttäjän syötettä.
        structure (list):
            Testausta varten luotu lista trie:n rakenteesta.
    """

    def __init__(self):
        """Luokan konstruktori.

        Alustaa TrieNoden, sekä tyhjät muuttujat
        """

        self.root = TrieNode('')
        self.words = []
        self.structure = []

    def add_word(self, word):
        """Lisää sanan trie-tietorakenteeseen.

        Args:
            word: Lisättävä sana.
        """

        current = self.root
        for char in word:
            if char in current.child:
                current = current.child[char]
            else:
                new_char = TrieNode(char)
                current.child[char] = new_char
                current = new_char
        current.finish = True

    def search_word(self, word):
        """Hakee sanaa trie-tietorakenteesta.

        Args:
            word: Haettava sana.

        Returns:
            bool: False, jos sanan kirjainta ei löydy edellisen kirjaimen lapsista.
        """

        current = self.root
        for char in word:
            if char not in current.child:
                return False
            current = current.child[char]
        return current.finish

    def helper(self, current, prefix, words):
        """Käy läpi trie-tietorakenneta ja lisää sanat listaan.
        
        Metodi käy solmuja yksitellen läpi, ja lisää kirjaimia merkkijonoon. Jos solmun finish arvo on True, lisätää sana listaan.

        Args:
            current: Läpikäytävä solmu, alustavasti juurisolmu.
            prefix: Merkkijono, joka lisätään listaan.
            words: Lista, mihin sanat lisätään.
        """

        if current.finish:
            words.append(prefix)
        for char, c in current.child.items():
            self.helper(c, prefix + char, words)

    def get_all_words(self):
        """Kutsuu helper -metodia parametreillä juurisolmu, tyhjä merkkijono ja sanalista.

        Returns:
            self.words: Sanalista.
        """

        current = self.root
        self.helper(current, "", self.words)
        return self.words

    def pre_order_traversal(self, node):
        """Käy läpi trie-tietorakennetaa ja lisää sanat listaan syvyyshaun esijärjestyksessä (pre-order).

        Args:
            node: Läpikäytävä solmu.
        """

        self.structure.append(node.value)

        for _, child_node in node.child.items():
            self.pre_order_traversal(child_node)

    def check_correct_structure(self):
        """Kutsuu metodia pre_order_traversal juurisolmulla ja palauttaa syvyyshaun tuottaman listan.

        Returns:
            self.structure: Lista merkkijonojen kirjaimista syvyyshaun mukaisessa järjestyksessä.
        """

        self.pre_order_traversal(self.root)
        return self.structure

    def __str__(self):
        """Muodostaa merkkijonomuotoisen esityksen merkkijonoista syvyyshaun mukaisessa järjestyksessä.

        Returns:
            str: Merkkijonojen merkit.
        """

        return ', '.join(self.structure)