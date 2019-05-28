class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        return [int(x, 2) for x in self.helper(n)]
    
    def helper(self, n):
        if n == 1:
            return ['0', '1']
        temp = self.helper(n - 1)
        return ['0' + x for x in temp] + ['1' + y for y in temp[::-1]]