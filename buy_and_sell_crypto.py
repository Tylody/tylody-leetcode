# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# Return the maximum profit you can achieve. You may choose to not make any transactions, in which case the profit would be 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(len(prices) - i - 1):
                profit = prices[j+i+1] - prices[i]

                if profit > max_profit:
                    max_profit = profit

        return max_profit