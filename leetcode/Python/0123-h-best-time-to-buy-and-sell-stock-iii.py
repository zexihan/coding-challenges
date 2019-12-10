class Solution_1:
    def maxProfit(self, prices: List[int]) -> int:
        hold1, hold2 = float('-inf'), float('-inf')
        release1, release2 = 0, 0
        for i in prices:
            # The maximum if we've just sold 2nd stock so far.
            release2 = max(release2, hold2 + i)
            # The maximum if we've just buy  2nd stock so far.
            hold2 = max(hold2, release1 - i)
            # The maximum if we've just sold 1nd stock so far.
            release1 = max(release1, hold1 + i)
            # The maximum if we've just buy  1st stock so far. 
            hold1 = max(hold1, -i)
        #Since release1 is initiated as 0, so release2 will always higher than release1.
        return release2

"""
f[k, ii] represents the max profit up until prices[ii] (Note: NOT ending with prices[ii]) using at most k transactions. 
f[k, ii] = max(f[k, ii-1], prices[ii] - prices[jj] + f[k-1, jj]) { jj in range of [0, ii-1] }
         = max(f[k, ii-1], prices[ii] + max(f[k-1, jj] - prices[jj]))
f[0, ii] = 0; 0 times transation makes 0 profit
f[k, 0] = 0; if there is only one price data point you can't make any money no matter how many times you can trade
"""
class Solution_2:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0: return 0
        K = 2 # number of max transation allowed
        maxProf = 0
        f = [[0] * len(prices)] * (K + 1)
        for kk in range(1,K + 1):
            tmpMax = f[kk-1][0] - prices[0]
            for ii in range(1,len(prices)):
                f[kk][ii] = max(f[kk][ii-1], prices[ii] + tmpMax)
                tmpMax = max(tmpMax, f[kk-1][ii] - prices[ii])
                maxProf = max(f[kk][ii], maxProf)

        return maxProf