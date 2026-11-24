class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        if n1 == 0:
            return 0

        s1_count = 0
        s2_count = 0
        index = 0

        # Store: index in s2 -> (s1_count, s2_count)
        seen = {}

        while s1_count < n1:
            s1_count += 1

            for char in s1:
                if char == s2[index]:
                    index += 1

                    if index == len(s2):
                        s2_count += 1
                        index = 0

            if index in seen:
                previous_s1_count, previous_s2_count = seen[index]

                # Counts before and inside the repeating cycle
                pre_s1 = previous_s1_count
                pre_s2 = previous_s2_count

                cycle_s1 = s1_count - previous_s1_count
                cycle_s2 = s2_count - previous_s2_count

                remaining_s1 = n1 - pre_s1
                cycles = remaining_s1 // cycle_s1

                s1_count = pre_s1 + cycles * cycle_s1
                s2_count = pre_s2 + cycles * cycle_s2

                # Process any remaining s1 blocks
                while s1_count < n1:
                    s1_count += 1

                    for char in s1:
                        if char == s2[index]:
                            index += 1

                            if index == len(s2):
                                s2_count += 1
                                index = 0

                return s2_count // n2

            else:
                seen[index] = (s1_count, s2_count)

        return s2_count // n2