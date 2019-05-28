class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        l = []
        candidates = sorted(candidates)
        self.backtrack(l, [], candidates, target, 0)
        return l
    
    def backtrack(self, l, tempL, candidates, remain, start):
        """
        :type l: List[List[int]]
        :type tempL: List[int]
        :type candidates: List[int]
        :type remain: int
        :type start: int
        """
        if remain < 0: 
            return None
        elif remain == 0: 
            l.append(list(tempL))
        else:
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]: 
                    continue
                tempL.append(candidates[i])
                self.backtrack(l, tempL, candidates, remain - candidates[i], i+1)
                tempL.pop()