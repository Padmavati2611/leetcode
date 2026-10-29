class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        import bisect

        sub = []

        for num in nums:
            i = bisect.bisect_left(sub, num)

            if i == len(sub):
                sub.append(num)
            else:
                sub[i] = num

        return len(sub)