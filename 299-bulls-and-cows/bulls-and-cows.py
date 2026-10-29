from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1

        secret_count = Counter(secret)
        guess_count = Counter(guess)

        matches = sum((secret_count & guess_count).values())
        cows = matches - bulls

        return f"{bulls}A{cows}B"