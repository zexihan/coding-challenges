"""
DFS
"""
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        result = []
        self.helper(result, [], 2, n)
        return result

    def helper(self, result, path, start, remain):
        if remain <= 1:
            if len(path) > 1:
                result.append(path[:])
            return

        import math
        for i in range(start, int(math.sqrt(remain)) + 1):
            if remain % i == 0:
                path.append(i)
                self.helper(result, path, i, remain // i)
                path.pop()

        if remain >= start:
            path.append(remain)
            self.helper(result, path, remain, 1)
            path.pop()
