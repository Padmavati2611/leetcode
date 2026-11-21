class Solution:
    def originalDigits(self, s: str) -> str:
        count = [0] * 10

        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        count[0] = freq[ord('z') - ord('a')]
        count[2] = freq[ord('w') - ord('a')]
        count[4] = freq[ord('u') - ord('a')]
        count[6] = freq[ord('x') - ord('a')]
        count[8] = freq[ord('g') - ord('a')]

        count[3] = freq[ord('h') - ord('a')] - count[8]
        count[5] = freq[ord('f') - ord('a')] - count[4]
        count[7] = freq[ord('s') - ord('a')] - count[6]
        count[1] = freq[ord('o') - ord('a')] - count[0] - count[2] - count[4]

        count[9] = freq[ord('i') - ord('a')] - count[5] - count[6] - count[8]

        result = ""
        for i in range(10):
            result += str(i) * count[i]

        return result