class Solution:
    def circularArrayLoop(self, nums):
        n = len(nums)

        def get_next(i, forward):
            # Must move in the same direction
            if nums[i] == 0 or (nums[i] > 0) != forward:
                return -1

            next_i = (i + nums[i]) % n

            # A cycle of length 1 is not allowed
            if next_i == i:
                return -1

            return next_i

        for i in range(n):
            if nums[i] == 0:
                continue

            forward = nums[i] > 0

            slow = i
            fast = i

            # Floyd's cycle detection
            while True:
                slow = get_next(slow, forward)
                if slow == -1:
                    break

                fast = get_next(fast, forward)
                if fast == -1:
                    break

                fast = get_next(fast, forward)
                if fast == -1:
                    break

                if slow == fast:
                    return True

            # Mark only indices moving in the same direction
            current = i

            while (
                nums[current] != 0
                and (nums[current] > 0) == forward
            ):
                next_current = (current + nums[current]) % n

                if next_current == current:
                    nums[current] = 0
                    break

                nums[current] = 0
                current = next_current

        return False