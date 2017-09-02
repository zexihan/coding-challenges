# Time: O(4^n)
# Space: O(4mn)
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        w = list(word)
        for y in range(len(board)):
            for x in range(len(board[y])):
                if self.check(board, y, x, w, 0):
                    return True
        return False

    def check(self, board, y, x, word, i):
        if i == len(word): return True
        if y < 0 or x < 0 or y == len(board) or x == len(board[y]): return False
        if board[y][x] != word[i]: return False
        board[y][x] = 0
        ifExist = self.check(board, y, x+1, word, i+1) or self.check(board, y, x-1, word, i+1) or self.check(board, y+1, x, word, i+1) or self.check(board, y-1, x, word, i+1)
        board[y][x] = word[i]
        return ifExist