class DamerauLevenshtein:
    def __init__(self):
        pass

    def edit_distance(self, word, compare_word):
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

                if i > 1 and j > 1 and word[i] == compare_word[j - 1] and word[i - 1] == compare_word[j]:
                    word_matrix[i][j] = min(
                        # transposition
                        word_matrix[i][j], word_matrix[i - 2][j - 2] + 1)

        return word_matrix[word_length][compare_word_length]
