"""
DP
max subarray product ends with a[j]: f[j] = max(a[j], max(a[j] * f[j-1], a[j] * g[j-1]) | j > 0)
min subarray product ends with a[j]: g[j] = min(a[j], min(a[j] * f[j-1], a[j] * g[j-1]) | j > 0)
j > 0
f[0], g[0], f[1], g[1], f[2], g[2], ..., f[n-1], g[n-1]
result is max(f[0], f[1], f[2], ..., f[n-1])
Time : O(n)
"""
class Solution_1:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums) 
        if n == 0:
            return 0
        
        f = [0] * n
        g = [0] * n
        res = - float('inf')
        for i in range(n):
            f[i] = nums[i]
            if i > 0:
                f[i] = max(f[i], max(nums[i] * f[i - 1], nums[i] * g[i - 1]))
            
            g[i] = nums[i]
            if i > 0:
                g[i] = min(g[i], min(nums[i] * f[i - 1], nums[i] * g[i - 1]))

            res = max(res, f[i])
        
        return res


class Solution_2:
    def maxProduct(self, nums: List[int]) -> int:
        # store the result that is the max we have found so far
        r = nums[0]

        # imax/imin stores the max/min product of
        # subarray that ends with the current number nums[i]
        imax, imin = r, r
        for i in range(1, len(nums)):
            # multiplied by a negative makes big number smaller, small number bigger
            # so we redefine the extremums by swapping them
            if nums[i] < 0:
                tmp = imax
                imax = imin
                imin = tmp

            # max/min product for the current number is either the current number itself
            # or the max/min by the previous number times the current one
            imax = max(nums[i], imax * nums[i])
            imin = min(nums[i], imin * nums[i])

            # the newly computed max value is a candidate for our global result
            r = max(r, imax)
        return r