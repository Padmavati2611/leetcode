
from collections import defaultdict
from math import gcd

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)

        if n <= 2:
            return n

        ans = 0

        for i in range(n):
            slopes = defaultdict(int)
            duplicates = 1
            best = 0

            for j in range(i + 1, n):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0 and dy == 0:
                    duplicates += 1
                    continue

                g = gcd(dx, dy)
                dx //= g
                dy //= g

                if dx < 0:
                    dx = -dx
                    dy = -dy

                elif dx == 0:
                    dy = 1

                slopes[(dx, dy)] += 1
                best = max(best, slopes[(dx, dy)])

            ans = max(ans, best + duplicates)

        return ans
