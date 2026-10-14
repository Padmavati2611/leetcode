
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = sorted(nums1 + nums2)
        n = len(nums)

        if n % 2 == 1:
            return float(nums[n // 2])
        else:
            mid = n // 2
            return (nums[mid - 1] + nums[mid]) / 2