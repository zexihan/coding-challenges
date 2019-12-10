"""
Iteration
Time: O(logn)
"""
class Solution_1:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0: return False
        while n % 2 == 0: n /= 2
        return n == 1

"""
Bit operation
Time: O(1)
"""
class Solution_2:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0: return False
        return n&(n-1) == 0