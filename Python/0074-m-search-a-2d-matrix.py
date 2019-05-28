# Time: O(log(mn))
# Space: O(1)
"""
Binary Seach in 1D Array
2D -> 1D: (i, j) -> index = i * n + j
1D -> 2D: index -> i = index / n; j = index % n 
"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False

        m = len(matrix)
        n = len(matrix[0])
        start = 0
        end = m * n - 1
        while end >= start:
            mid = start + (end - start) // 2

            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False