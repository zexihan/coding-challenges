class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        list = []
        self.backtrack(list,"",0,0,n)
        return list
    
    def backtrack(self,list,str,open,close,max):
        if len(str) == max * 2:
            list.append(str)
            return
        if open < max:
            self.backtrack(list,str+"(",open+1,close,max)
        if close < open:
            self.backtrack(list,str+")",open,close+1,max)