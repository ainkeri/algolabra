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
    """
    def __init__(self):
        self.root = TrieNode('')

    def add_word(self, word):
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
        current = self.root
        for char in word:
            if char not in current.child:
                return False
            current = current.child[char]
        return current.finish