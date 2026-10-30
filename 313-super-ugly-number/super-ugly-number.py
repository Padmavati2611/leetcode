
class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        ugly = [1] * n
        k = len(primes)

        pointers = [0] * k
        values = primes[:]

        for i in range(1, n):
            next_ugly = min(values)
            ugly[i] = next_ugly

            for j in range(k):
                if values[j] == next_ugly:
                    pointers[j] += 1
                    values[j] = primes[j] * ugly[pointers[j]]

        return ugly[n - 1]
