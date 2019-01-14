# DP
# f[X] = min{f[X-2] + 1, f[X-5] + 1, f[X-7] + 1}
# f[0] = 0; If Y cannot be made up, f[Y] = inf
# Time: O(n)
# Space: O(n)
class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        n = len(coins)
        f = [float('inf')] * (amount + 1)

        # initialization
        f[0] = 0
        for i in range(1, amount + 1):
            # last coin coins[k]
            for k in range(n):
                # boundary
                if i >= coins[k] and f[i-coins[k]] != float('inf'):
                    f[i] = min(f[i], f[i - coins[k]] + 1)

        if f[amount] == float('inf'):
            return -1
        else:
            return f[amount]


