"""
DP
Time: O(n)
Space: O(n)
"""
import math
class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        notPrime = [False] * n
        bound = math.sqrt(n)
        count = 0
        for i in range(2,n):
            if not notPrime[i]:
                count += 1
            if i <= bound:
                for j in range(i**2, n, i):
                    if not notPrime[j]:
                        notPrime[j] = True
        return count