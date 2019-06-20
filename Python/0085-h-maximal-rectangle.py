"""
Maximum Height at Each Point
Keep track of h, l, r of each point in the row
* new_height[j] = old_height[j] + 1 if row[j] == '1' else 0
* new_left[j] = max(old_left[j], cur_left)
* new_right[j] = min(old_right[j], cur_right)
area = height[j] * (right[j] - left[j])
Time: O(NM)
Space: O(M)
"""
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])

        left = [0] * n
        right = [n] * n
        height = [0] * n

        maxarea = 0

        for i in range(m):
            cur_left, cur_right = 0, n
            # update height
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            # update left
            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1
            # update right
            for j in range(n - 1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            # update the area
            for j in range(n):
                maxarea = max(maxarea, height[j] * (right[j] - left[j]))

        return maxarea
