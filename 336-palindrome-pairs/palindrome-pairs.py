class Solution:
    def palindromePairs(self, words: list[str]) -> list[list[int]]:
        word_map = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            for j in range(len(word) + 1):
                prefix = word[:j]
                suffix = word[j:]

                # Check if prefix is a palindrome
                if prefix == prefix[::-1]:
                    rev = suffix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([word_map[rev], i])

                # Check if suffix is a palindrome
                if j != len(word) and suffix == suffix[::-1]:
                    rev = prefix[::-1]
                    if rev in word_map and word_map[rev] != i:
                        result.append([i, word_map[rev]])

        return result