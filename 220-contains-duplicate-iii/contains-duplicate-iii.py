
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff <= 0 or valueDiff < 0:
            return False

        buckets = {}
        width = valueDiff + 1

        for i, num in enumerate(nums):
            bucket_id = num // width

            if bucket_id in buckets:
                return True

            if bucket_id - 1 in buckets and num - buckets[bucket_id - 1] <= valueDiff:
                return True

            if bucket_id + 1 in buckets and buckets[bucket_id + 1] - num <= valueDiff:
                return True

            buckets[bucket_id] = num

            if i >= indexDiff:
                old_bucket = nums[i - indexDiff] // width
                del buckets[old_bucket]

        return False
