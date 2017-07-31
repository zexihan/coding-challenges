# Time: O(n)
# Space: O(n)
# Dynamic Programming
import math
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
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


if __name__ == "__main__":
    new = Solution()
    print(new.countPrimes(1500000)) # 6
