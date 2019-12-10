class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1: return s
        
        ret = ""
        n = len(s)
        cycleLen = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, n, cycleLen):
                if j + i < n:
                    ret += s[j + i]
                    if i != 0 and i != numRows - 1 and j + cycleLen - i < n:
                        ret+= s[j + cycleLen - i]
        return ret
