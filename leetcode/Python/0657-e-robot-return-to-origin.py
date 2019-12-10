class Solution:
    def judgeCircle(self, moves: str) -> bool:
        v = moves.count("U") - moves.count("D")
        h = moves.count("L") - moves.count("R")
        if v or h:
            return False
        else:
            return True
