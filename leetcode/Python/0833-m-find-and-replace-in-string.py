class Solution_1:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        res = ""
        mapper = {}
        for i in range(len(indexes)):
            mapper[indexes[i]] = (sources[i], targets[i])

        i = 0
        while i < len(S):
            if i in mapper and S[i: i + len(mapper[i][0])] == mapper[i][0]:
                res += mapper[i][1]
                i += len(mapper[i][0])
            else:
                res += S[i]
                i += 1
        return res

class Solution_2:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        for i, s, t in sorted(zip(indexes, sources, targets), reverse=True):
            if S[i:i + len(s)] == s:
                S = S[:i] + t + S[i + len(s):]
            else:
                S = S
        return S
