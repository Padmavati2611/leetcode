class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if not prices:
            return 0

        buy1 = float('inf')
        buy2 = float('inf')
        profit1 = 0
        profit2 = 0

        for price in prices:
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)

            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)

        return profit2