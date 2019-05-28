# Time:O(log3(n))
# Space: O(1)
class Solution_1:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False

        while n % 3 == 0:
            n //= 3

        return n == 1

# Time: Unknown
# Space: O(1)
import math
class Solution_2:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n < 1:
            return False
        return math.log10(n) / math.log10(3) % 1 == 0

'''
simply not working for python
math.log(sys.maxsize, 3) = 39
math.pow(3, 39) = 4.052555153018976e+18
3^39
Time: O(1)
Space: O(1)
'''
import sys
class Solution_3:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and math.pow(3, int(math.log(sys.maxsize, 3))) / n == 0
