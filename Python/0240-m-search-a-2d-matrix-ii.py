# Time: O(max(mlogn, nlogn))
"""
Right or Down of the mid
Find the valid range for next subproblem
Not real binary search, Recursion
"""
class Solution_1(object):
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

# Time: O(m+n)
"""
Find a position with only one choice
Top-right point
"""
class Solution_2(object):
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

if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))
    print(new_2.searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5))