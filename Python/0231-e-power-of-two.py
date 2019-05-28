# Iteration
# Time: O(logn)
class Solution_1(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0: return False
        while n % 2 == 0: n /= 2
        return n == 1

# Bit operation
# Time: O(1)
class Solution_2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0: return False
        return n&(n-1) == 0