import collections
class Solution:
    def wordsAbbreviation(self, dict: List[str]) -> List[str]:
        if not dict:
            return None
        
        n = len(dict)
        res = [0] * n
        prefix = [0] * n
        count = collections.defaultdict(int)

        for i in range(n):
            prefix[i] = 1
            res[i] = self.getAbbr(dict[i], 1)
            count[res[i]] += 1
        
        while True:
            unique = True
            for i in range(n):
                if count[res[i]] > 1:
                    prefix[i] += 1
                    res[i] = self.getAbbr(dict[i], prefix[i])
                    count[res[i]] += 1
                    unique = False
            
            if unique:
                break
        return res


    def getAbbr(self, s, p):
        if p >= len(s) - 2:
            return s
        return s[:p] + str(len(s) - 1 - p) + s[-1]