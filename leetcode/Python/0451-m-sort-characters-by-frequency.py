import collections
class Solution:
    def frequencySort(self, s: str) -> str:
        chrCnt = collections.Counter(s)
        sortedChrCnt = sorted(chrCnt.items(), key=lambda x: -x[1])
        return "".join(item[0] * item[1] for item in sortedChrCnt)
