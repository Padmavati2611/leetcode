class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        count = {}

        for a in nums1:
            for b in nums2:
                total = a + b
                count[total] = count.get(total, 0) + 1

        result = 0

        for c in nums3:
            for d in nums4:
                total = c + d
                result += count.get(-total, 0)

        return result