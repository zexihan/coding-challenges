"""
Invariant
"""
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start.replace('X', '') != end.replace('X', ''):
            return False

        startL, startR = [], []
        endL, endR = [], []
        for i in range(len(start)):
            if start[i] == 'L':
                startL.append(i)
            elif start[i] == 'R':
                startR.append(i)
            if end[i] == 'L':
                endL.append(i)
            elif end[i] == 'R':
                endR.append(i)

        for i in range(len(startL)):
            if startL[i] < endL[i]:
                return False
        for i in range(len(startR)):
            if startR[i] > endR[i]:
                return False

        return True
