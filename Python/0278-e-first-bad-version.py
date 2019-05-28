# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

# Time: O(logn), depth of the binary tree
# Space: O(1)
# Binary Search, iteration
class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, end = 1, n
        while start < end - 1:
            mid = start + (end - start) // 2
            if not isBadVersion(mid):
                start = mid
            else:
                end = mid
        return start if isBadVersion(start) else end
