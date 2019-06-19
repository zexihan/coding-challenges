"""
DP
f[Y]: the number of combinations that make up Y
f[0] = 1
f[X] = sum(f[X - c] for c in coins)
Time: O(S * n)
Space: O(S)
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        f = [0] * (amount + 1)
        f[0] = 1

        for c in coins:
            for i in range(c, amount + 1):
                f[i] += f[i - c]

        return f[amount]
