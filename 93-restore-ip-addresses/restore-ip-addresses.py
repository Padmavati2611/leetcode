class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        result = []

        def backtrack(start, parts):
            if len(parts) == 4:
                if start == len(s):
                    result.append(".".join(parts))
                return

            for length in range(1, 4):
                if start + length > len(s):
                    break

                part = s[start:start + length]

                if part[0] == '0' and length > 1:
                    continue

                if int(part) > 255:
                    continue

                backtrack(start + length, parts + [part])

        backtrack(0, [])
        return result