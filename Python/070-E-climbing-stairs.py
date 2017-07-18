# Time: O(n)
# Space: O(1)
# Dynamic Programming
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        if n == 1:
            return 1

        pre = 1
        cur = 2

        for i in range(2, n):
            tmp = cur
            cur = pre + cur
            pre = tmp
        return cur

if __name__ == "__main__":
    new = Solution()
    print(new.climbStairs(5))
