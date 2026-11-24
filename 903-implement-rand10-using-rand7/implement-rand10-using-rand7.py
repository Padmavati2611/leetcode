class Solution:
    def rand10(self):
        while True:
            # Generate a uniform random number from 1 to 49
            num = (rand7() - 1) * 7 + rand7()

            # Accept only numbers from 1 to 40
            if num <= 40:
                return (num - 1) % 10 + 1