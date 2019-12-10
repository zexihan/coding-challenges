"""
DP
f[Y]: the fewest number of coins needed to make up Y
f[0] = 0
f[X] = min{f[X-2], f[X-5], f[X-7]} + 1
If Y cannot be made up, f[Y] = inf
Time: O(S * n)
Space: O(S)
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # initialization
        f = [float('inf')] * (amount + 1)
        f[0] = 0

        for i in range(1, amount + 1):
            # current coin coins[k]
            for k in range(len(coins)):
                # boundary
                if i >= coins[k] and f[i-coins[k]] != float('inf'):
                    f[i] = min(f[i], f[i - coins[k]] + 1)

        return f[amount] if f[amount] != float('inf') else -1


