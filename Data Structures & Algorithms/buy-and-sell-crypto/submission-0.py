class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        slow = 0
        max_profit = 0

        for fast in range(len(prices)):
            profit = prices[fast] - prices[slow]
            max_profit = max(max_profit, profit)

            if prices[fast] < prices[slow]:
                slow = fast
        return max_profit
