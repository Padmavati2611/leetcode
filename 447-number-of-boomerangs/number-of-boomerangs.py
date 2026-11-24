class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        result = 0

        for i in range(len(points)):
            distance_count = {}

            x1, y1 = points[i]

            for j in range(len(points)):
                if i == j:
                    continue

                x2, y2 = points[j]

                distance = (x1 - x2) ** 2 + (y1 - y2) ** 2

                distance_count[distance] = distance_count.get(distance, 0) + 1

            for count in distance_count.values():
                result += count * (count - 1)

        return result