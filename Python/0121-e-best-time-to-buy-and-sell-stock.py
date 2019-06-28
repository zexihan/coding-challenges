class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        best = float('-inf')
        minPrice = prices[0]
        for i in range(len(prices)):
            minPrice = min(minPrice, prices[i])
            best = max(best, prices[i] - minPrice)
        return best