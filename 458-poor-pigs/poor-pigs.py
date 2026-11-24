class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        if buckets == 1:
            return 0

        rounds = minutesToTest // minutesToDie
        states = rounds + 1

        pigs = 0
        combinations = 1

        while combinations < buckets:
            pigs += 1
            combinations *= states

        return pigs