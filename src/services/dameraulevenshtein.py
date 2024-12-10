class DamerauLevenshtein:
    """Luokka, joka vertaa kahden annetun sanan etäisyyttä toisiinsa."""

    def edit_distance(self, word, compare_word):
        """Vertaa kahden sanan etäisyyttä toisiinsa.

        Molemmille sanoille luodaan matriisit, joiden avulla verrataan parhain mahdollinen etäisyys.
        Etäisyys määritetään merkkien poistojen, lisäysten, korvausten ja transpositioiden
        perusteella. Merkkien korvaamisessa huomioidaan tarkemmin kirjaimet, jotka ovat
        näppäimistöllä lähimpänä läpikäytävää merkkiä.

        Args:
            word (str): Ensimmäinen vertailtava sana (käyttäjän syöte).
            compare_word (str): Toinen vertailtava sana (sana trie-tietorakenteesta).

        Returns:
            int: Damerau-Levenshtein -etäisyys sanojen välillä.
        """

        closest_keyboard_letters = {
            "a": ["q", "w", "s", "z"],
            "b": ["v", "g", "h", "n"],
            "c": ["x", "d", "f", "v"],
            "d": ["s", "e", "r", "f", "c", "x"],
            "e": ["w", "s", "d", "r"],
            "f": ["d", "r", "t", "g", "v", "c"],
            "g": ["f", "t", "y", "h", "b", "v"],
            "h": ["g", "y", "u", "j", "n", "b"],
            "i": ["u", "j", "k", "o"],
            "j": ["h", "u", "i", "k", "m", "n"],
            "k": ["j", "i", "o", "l", ",", "m"],
            "l": ["k", "o", "p", "ö", ".", ","],
            "m": ["n", "j", "k", ","],
            "n": ["b", "h", "j", "m"],
            "o": ["i", "k", "l", "p"],
            "p": ["o", "l", "ö", "å"],
            "q": ["w", "a"],
            "r": ["e", "d", "f", "t"],
            "s": ["a", "w", "e", "d", "x", "z"],
            "t": ["r", "f", "g", "y"],
            "u": ["y", "h", "j", "i"],
            "v": ["c", "f", "g", "b"],
            "w": ["q", "a", "s", "e"],
            "x": ["z", "s", "d", "c"],
            "y": ["t", "g", "h", "u"],
            "z": ["a", "s", "x"],
            "å": ["p", "ö", "ä"],
            "ä": ["ö", "å"],
            "ö": ["l", "p", "å", "ä"],
        }

        word = " " + word
        compare_word = " " + compare_word

        word_length = len(word) - 1
        compare_word_length = len(compare_word) - 1

        word_matrix = [[0] * (compare_word_length + 1) for _ in range(word_length + 1)]

        for i in range(word_length + 1):
            word_matrix[i][0] = i
        for j in range(compare_word_length + 1):
            word_matrix[0][j] = j

        for i in range(1, word_length + 1):
            for j in range(1, compare_word_length + 1):
                if word[i] == compare_word[j]:
                    cost = 0
                else:
                    cost = 1

                word_matrix[i][j] = min(
                    word_matrix[i - 1][j] + 1,  # deletion
                    word_matrix[i][j - 1] + 1,  # insertion
                    word_matrix[i - 1][j - 1] + cost,  # substitution
                )

                if i == j:
                    if word[i] in closest_keyboard_letters.get(
                        compare_word[j].lower(), "Unknown"
                    ):
                        word_matrix[i][j] = (
                            word_matrix[i - 1][j - 1] + 0.25
                        )  # substitution with adjacent letter in keyboard

                if (
                    i > 1
                    and j > 1
                    and word[i] == compare_word[j - 1]
                    and word[i - 1] == compare_word[j]
                ):
                    word_matrix[i][j] = min(
                        # transposition
                        word_matrix[i][j],
                        word_matrix[i - 2][j - 2] + 1,
                    )

        return word_matrix[word_length][compare_word_length]
