
class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)

        max_digits = num.bit_length()

        for m in range(max_digits, 1, -1):
            left = 2
            right = int(num ** (1 / (m - 1))) + 1

            while left <= right:
                base = (left + right) // 2

                total = 1
                value = 1

                for _ in range(m - 1):
                    value *= base
                    total += value

                    if total > num:
                        break

                if total == num:
                    return str(base)

                if total < num:
                    left = base + 1
                else:
                    right = base - 1

        return str(num - 1)
