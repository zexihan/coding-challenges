"""
first reverse up to down, then swap the symmetry 
 1 2 3     7 8 9     7 4 1
 4 5 6  => 4 5 6  => 8 5 2
 7 8 9     1 2 3     9 6 3
Time: O(n^2)
Space: O(1)
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        return matrix