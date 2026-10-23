class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [""]

            if start in memo:
                return memo[start]

            result = []

            for end in range(start + 1, len(s) + 1):
                word = s[start:end]

                if word in word_set:
                    for suffix in backtrack(end):
                        result.append(
                            word if not suffix else word + " " + suffix
                        )

            memo[start] = result
            return result

        return backtrack(0)