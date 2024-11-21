class DamerauLevenshtein:
    """Luokka, joka vertaa kahden annetun sanan etäisyyttä toisiinsa.
    """

    def edit_distance(self, word, compare_word):
        """Vertaa kahden sanan etäisyyttä toisiinsa.

        Molemmille sanoille luodaan matriisit, joiden avulla verrataan parhain mahdollinen etäisyys.
        Etäisyys määritetän merkkien poistojen, lisäysten, korvausten ja transpositioiden
        perusteella.

        Args:
            word (str): Ensimmäinen vertailtava sana (käyttäjän syöte).
            compare_word (str): Toinen vertailtava sana (sana trie-tietorakenteesta).
        
        Returns:
            int: Damerau-Levenshtein -etäisyys sanojen välillä.
        """

        word = " " + word
        compare_word = " " + compare_word

        word_length = len(word) - 1
        compare_word_length = len(compare_word) - 1

        word_matrix = [[0] * (compare_word_length + 1)
                       for _ in range(word_length + 1)]

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
                    word_matrix[i - 1][j] + 1,    # deletion
                    word_matrix[i][j - 1] + 1,    # insertion
                    word_matrix[i - 1][j - 1] + cost    # substitution
                )

                if i > 1 and j > 1 and word[i] == compare_word[j - 1] and word[i - 1] == compare_word[j]: # pylint: disable=line-too-long
                    word_matrix[i][j] = min(
                        # transposition
                        word_matrix[i][j], word_matrix[i - 2][j - 2] + 1)

        return word_matrix[word_length][compare_word_length]
