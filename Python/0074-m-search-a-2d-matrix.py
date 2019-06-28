"""
Binary Seach in 1D Array
2D -> 1D: (i, j) -> index = i * n + j
1D -> 2D: index -> i = index / n; j = index % n 
Time: O(log(mn))
Space: O(1)
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        start, end = 0, n * m - 1
        
        while start + 1 < end:
            mid = start + (end - start) // 2
            row = mid // m
            col = mid % m
            if matrix[row][col] < target:
                start = mid
            else:
                end = mid
        
        if matrix[start // m][start % m] == target:
            return True
        if matrix[end // m][end % m] == target:
            return True
        
        return False