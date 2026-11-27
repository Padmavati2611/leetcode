
class Solution:
    def magicalString(self, n: int) -> int:
        if n <= 0:
            return 0

        s = [1, 2, 2]

        count = 1
        index = 2
        num = 1

        while len(s) < n:
            for _ in range(s[index]):
                s.append(num)

                if num == 1 and len(s) <= n:
                    count += 1

            num = 3 - num
            index += 1

        return count
