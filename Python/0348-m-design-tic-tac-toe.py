class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.rows = [0 for i in range(n)]
        self.cols = [0 for i in range(n)]
        self.diagonal = 0
        self.antiDiagonal = 0


    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        toAdd = 1 if player == 1 else -1

        self.rows[row] += toAdd
        self.cols[col] += toAdd

        if row == col:
            self.diagonal += toAdd

        if col == len(self.cols) - row - 1:
            self.antiDiagonal += toAdd

        size = len(self.rows)
        if abs(self.rows[row]) == size or abs(self.cols[col]) == size or abs(self.diagonal) == size or abs(self.antiDiagonal) == size:
            return player

        return 0


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
