class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = list(range(1, n + 1))
        k -= 1
        result = []

        fact = 1
        for i in range(1, n):
            fact *= i

        while numbers:
            index = k // fact
            result.append(str(numbers.pop(index)))
            k %= fact

            if numbers:
                fact //= len(numbers)

        return "".join(result)