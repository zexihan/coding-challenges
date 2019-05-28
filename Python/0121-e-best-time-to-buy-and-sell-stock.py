class Solution_1(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxCur, maxSoFar = 0, 0
        for i in range(1, len(prices)):
            maxCur = max(0, maxCur + prices[i] - prices[i-1])
            maxSoFar = max(maxCur, maxSoFar)
        return maxSoFar

class Solution_2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        max, min = 0, prices[0]
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > profit:
                profit = prices[i] - min
        return profit

if __name__ == "__main__":
    new = Solution_1()
    print(new.maxProfit([7, 1, 5, 3, 6, 4])) # 5 = 5 - 1 + 3 - 5 + 6 - 3