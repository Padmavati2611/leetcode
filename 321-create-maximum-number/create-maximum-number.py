
class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:

        def maxSubsequence(nums, t):
            stack = []
            drop = len(nums) - t

            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1

                stack.append(num)

            return stack[:t]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        result = []

        start = max(0, k - len(nums2))
        end = min(k, len(nums1))

        for i in range(start, end + 1):
            a = maxSubsequence(nums1, i)
            b = maxSubsequence(nums2, k - i)

            candidate = merge(a[:], b[:])

            if candidate > result:
                result = candidate

        return result
