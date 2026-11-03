class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0

        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for char in freq:
            if freq[char] < k:
                return max(
                    self.longestSubstring(sub, k)
                    for sub in s.split(char)
                )

        return len(s)