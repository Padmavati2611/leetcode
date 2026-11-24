class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        from collections import Counter

        if len(p) > len(s):
            return []

        p_count = Counter(p)
        window = Counter(s[:len(p)])

        result = []

        if window == p_count:
            result.append(0)

        for i in range(len(p), len(s)):
            # Add new character
            window[s[i]] += 1

            # Remove character leaving the window
            left_char = s[i - len(p)]
            window[left_char] -= 1

            if window[left_char] == 0:
                del window[left_char]

            # Check if current window is an anagram
            if window == p_count:
                result.append(i - len(p) + 1)

        return result