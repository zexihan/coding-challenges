"""
Right or Down of the mid
Find the valid range for next subproblem
Not real binary search, Recursion
Time: O(max(mlogn, nlogn))
"""
class Solution_1:
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
        return self.binarySearch(matrix, target, 0, 0, m - 1, n - 1)

    def binarySearch(self, matrix, target, startX, startY, endX, endY):
        # base case: start point goes beyond
        if startX > endX or startY > endY:
            return False
        
        midX = startX + (endX - startX) // 2
        midY = startY + (endY - startY) // 2

        # case 1: found
        if matrix[midX][midY] == target:
            return True
        # case 2: larger than target, go into left or up submatrix
        elif matrix[midX][midY] > target:
            return self.binarySearch(matrix, target, startX, startY, endX, midY - 1) or self.binarySearch(matrix, target, startX, midY, midX - 1, endY)
        # case 3: smaller than target, go into right or down submatrix
        else:
            return self.binarySearch(matrix, target, startX, midY + 1, endX, endY) or self.binarySearch(matrix, target, midX + 1, startY, endX, midY)


"""
Find a position with only one choice
Top-right point
Time: O(m+n)
"""
class Solution_2:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        row = len(matrix)
        col = len(matrix[0])

        # start from the top-right point
        curRow = 0
        curCol = col - 1
        while curRow < row and curCol >= 0:
            # larger than target -> go left
            if matrix[curRow][curCol] > target:
                curCol -= 1
            # smaller than target -> go down
            elif matrix[curRow][curCol] < target:
                curRow += 1
            else:
                return True
        return False
