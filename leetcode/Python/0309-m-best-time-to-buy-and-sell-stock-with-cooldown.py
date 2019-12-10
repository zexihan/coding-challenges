"""
dp

sells[i]表示在第i天不持有股票所能获得的最大累计收益
buys[i]表示在第i天持有股票所能获得的最大累计收益

初始化数组：
sells[0] = 0
sells[1] = max(0, prices[1] - prices[0])
buys[0] = -prices[0]
buys[1] = max(-prices[0], -prices[1])

状态转移方程：
sells[i] = max(sells[i - 1], buys[i-1] + prices[i])
buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])

所求最大收益为sells[-1]

Time: O(n)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size < 2:
            return 0
        sells = [None] * size
        buys = [None] * size
        sells[0], sells[1] = 0, max(0, prices[1] - prices[0])
        buys[0], buys[1] = -prices[0], max(-prices[0], -prices[1])
        for i in range(2, size):
            sells[i] = max(sells[i - 1], buys[i-1] + prices[i])
            buys[i] = max(buys[i - 1], sells[i - 2] - prices[i])
        return sells[-1]
