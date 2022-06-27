# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        L = 0
        R = 1
        maximum_profit = 0
        while R < len(prices):
            if prices[L] < prices[R]:
                profit = prices[R] - prices[L]
                maximum_profit = max(maximum_profit, profit)
            else:
                L = R
            R += 1
        return maximum_profit
