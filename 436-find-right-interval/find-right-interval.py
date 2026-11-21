class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        starts = sorted((interval[0], i) for i, interval in enumerate(intervals))

        result = []

        import bisect

        for interval in intervals:
            pos = bisect.bisect_left(starts, (interval[1], 0))

            if pos < len(starts):
                result.append(starts[pos][1])
            else:
                result.append(-1)

        return result