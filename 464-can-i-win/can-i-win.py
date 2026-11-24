from functools import lru_cache

class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        if desiredTotal <= 0:
            return True

        total_sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2

        if total_sum < desiredTotal:
            return False

        @lru_cache(None)
        def can_win(used, remaining):
            for num in range(1, maxChoosableInteger + 1):
                bit = 1 << num

                # Skip numbers that have already been chosen
                if used & bit:
                    continue

                # If this number reaches the target, we win
                if num >= remaining:
                    return True

                # If the opponent cannot win after this choice,
                # then we can win
                if not can_win(used | bit, remaining - num):
                    return True

            return False

        return can_win(0, desiredTotal)