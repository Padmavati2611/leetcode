class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        result = []
        i = 0
        n = len(words)

        while i < n:
            j = i
            line_length = 0

            # Find the maximum number of words that fit in this line
            while j < n and line_length + len(words[j]) + (j - i) <= maxWidth:
                line_length += len(words[j])
                j += 1

            num_words = j - i
            total_spaces = maxWidth - line_length

            # Last line or line with only one word: left-justify
            if j == n or num_words == 1:
                line = " ".join(words[i:j])
                line += " " * (maxWidth - len(line))

            else:
                spaces = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)

                line = ""

                for k in range(i, j - 1):
                    line += words[k]
                    line += " " * (spaces + (1 if k - i < extra_spaces else 0))

                line += words[j - 1]

            result.append(line)
            i = j

        return result