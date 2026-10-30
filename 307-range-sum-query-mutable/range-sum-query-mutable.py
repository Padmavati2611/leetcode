
class NumArray:

    def __init__(self, nums: list[int]):
        self.n = len(nums)
        self.nums = nums[:]
        self.tree = [0] * (self.n + 1)

        for i in range(self.n):
            self.add(i, nums[i])

    def add(self, index, val):
        index += 1
        while index <= self.n:
            self.tree[index] += val
            index += index & -index

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.add(index, diff)

    def prefixSum(self, index):
        total = 0
        index += 1

        while index > 0:
            total += self.tree[index]
            index -= index & -index

        return total

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixSum(right) - self.prefixSum(left - 1)
