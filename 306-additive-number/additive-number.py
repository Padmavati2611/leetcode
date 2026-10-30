
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i + 1, n):
                a = num[:i]
                b = num[i:j]

                if (len(a) > 1 and a[0] == '0') or \
                   (len(b) > 1 and b[0] == '0'):
                    continue

                x, y = int(a), int(b)
                k = j

                while k < n:
                    total = x + y
                    s = str(total)

                    if not num.startswith(s, k):
                        break

                    k += len(s)
                    x, y = y, total

                if k == n:
                    return True

        return False
