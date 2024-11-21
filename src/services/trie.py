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
            Trie-rakenteen juurisolmu.
    """

    def __init__(self):
        self.root = TrieNode('')
        self.words = []
        self.structure = []

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

    def helper(self, current, prefix, words):
        if current.finish:
            words.append(prefix)
        for char, c in current.child.items():
            self.helper(c, prefix + char, words)

    def get_all_words(self):
        current = self.root
        self.helper(current, "", self.words)
        return self.words

    def pre_order_traversal(self, node):
        self.structure.append(node.value)

        for _, child_node in node.child.items():
            self.pre_order_traversal(child_node)

    def check_correct_structure(self):
        self.pre_order_traversal(self.root)
        return self.structure

    def __str__(self):
        return ', '.join(self.structure)