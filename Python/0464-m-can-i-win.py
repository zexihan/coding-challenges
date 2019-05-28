class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        def win(M, T, m, state):
            if T <= 0:
                return False
            if m[state] != 0:
                return m[state] == 1
            for i in range(M):
                if (state & (1 << i)) > 0:  # number i used
                    continue
                # The next player can not win, current player wins
                if not win(M, T - i - 1, m, state | (1 << i)):
                    m[state] = 1
                    return True
            # Current player loses.
            m[state] = -1
            return False

        M = maxChoosableInteger
        T = desiredTotal
        s = M * (M + 1) / 2
        if s < T:
            return False
        if T <= 0:
            return True
        if s == T:
            return (M % 2) == 1

        m = [0] * (1 << M)  # 0: unknown, 1: won, -1: lost
        return win(M, T, m, 0)
