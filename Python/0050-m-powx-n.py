"""
Recursion
Time: O(logn)
Space: O(logn)
"""
class Solution_1:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1 / x
        return self.myPow(x * x, n // 2) if n % 2 == 0 else x * self.myPow(x * x, n // 2)

"""
Binary a^(1010)2 = a^(1000)2 * a^(10)2
Time: O(logn)
Space: O(1)
"""
class Solution_2:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = -n
        res = 1
        tmp = x # x^1, x^2, x^4, x^8...
        while n != 0:
            if n % 2 == 1:
                res *= tmp
            tmp *= tmp
            n //= 2
        return res