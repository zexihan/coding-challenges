class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        left, right = 1, x
        while True:
            mid = (left + right) // 2
            if mid * mid > x:
                right = mid - 1
            else:
                if (mid + 1) * (mid + 1) > x:
                    return mid
                left = mid + 1
