
class Solution:
    def findRadius(self, houses: list[int], heaters: list[int]) -> int:
        houses.sort()
        heaters.sort()

        left = 0
        right = max(
            max(houses) - min(heaters),
            max(heaters) - min(houses)
        )

        def can_cover(radius):
            i = 0

            for house in houses:
                while i < len(heaters) and heaters[i] < house - radius:
                    i += 1

                if i == len(heaters) or heaters[i] > house + radius:
                    return False

            return True

        while left < right:
            mid = (left + right) // 2

            if can_cover(mid):
                right = mid
            else:
                left = mid + 1

        return left
