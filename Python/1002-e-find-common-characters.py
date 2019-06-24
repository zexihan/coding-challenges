import collections
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        alphaCnt = collections.defaultdict(int)
        for c in A[0]:
            alphaCnt[c] += 1
        for w in A[1:]:
            wCnt = collections.Counter(w)
            for c in alphaCnt:
                alphaCnt[c] = min(alphaCnt[c], wCnt[c])
        res = []
        for c, cnt in alphaCnt.items():
            res.extend([c] * cnt)
        return res