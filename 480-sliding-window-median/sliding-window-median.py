
import heapq
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums: list[int], k: int) -> list[float]:
        small = []  # Max heap (negative values)
        large = []  # Min heap

        delayed = defaultdict(int)

        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap == small else heap[0]

                if delayed[num] > 0:
                    heapq.heappop(heap)
                    delayed[num] -= 1
                else:
                    break

        def balance():
            nonlocal small_size, large_size

            if small_size > large_size + 1:
                num = -heapq.heappop(small)
                heapq.heappush(large, num)

                small_size -= 1
                large_size += 1

                prune(small)

            elif small_size < large_size:
                num = heapq.heappop(large)
                heapq.heappush(small, -num)

                large_size -= 1
                small_size += 1

                prune(large)

        def add(num):
            nonlocal small_size, large_size

            if not small or num <= -small[0]:
                heapq.heappush(small, -num)
                small_size += 1
            else:
                heapq.heappush(large, num)
                large_size += 1

            balance()

        def remove(num):
            nonlocal small_size, large_size

            delayed[num] += 1

            if num <= -small[0]:
                small_size -= 1

                if num == -small[0]:
                    prune(small)
            else:
                large_size -= 1

                if large and num == large[0]:
                    prune(large)

            balance()

        def get_median():
            if k % 2 == 1:
                return float(-small[0])

            return (-small[0] + large[0]) / 2.0

        for i in range(k):
            add(nums[i])

        result = [get_median()]

        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])

            result.append(get_median())

        return result
