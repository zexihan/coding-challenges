"""
One iteration
Time: O(1)
Space: O(1)
"""
import collections
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [collections.defaultdict(int) for i in range(9)]
        columns = [collections.defaultdict(int) for i in range(9)]
        boxes = [collections.defaultdict(int) for i in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                if num != ".":
                    box_index = (i // 3) * 3 + j // 3

                    rows[i][num] += 1
                    columns[j][num] += 1
                    boxes[box_index][num] += 1

                    if rows[i][num] > 1 or columns[j][num] > 1 or boxes[box_index][num] > 1:
                        return False

        return True
