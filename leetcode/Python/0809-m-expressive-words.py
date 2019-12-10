class Solution:
    def expressiveWords(self, S: str, words: List[str]) -> int:
        slist, scount = self.rle(S)
        res = []
        for word in words:
            if len(word) > len(S):
                continue
            clist, ccount = self.rle(word)
            for i, j in zip(range(len(clist)), range(len(slist))):
                if clist[i] == slist[j] and (ccount[i] == scount[j] or scount[i] >= 3):
                    continue
                else:
                    break
            else:
                if j == len(slist) - 1:
                    res.append(clist[:])
        return len(res)

    def rle(self, S):
        if not S:
            return S
        chars = []
        counts = []
        count = 0
        for i in range(len(S)):
            if not chars:
                chars.append(S[i])
                count += 1
                continue
            if S[i] != chars[-1]:
                counts.append(count)
                chars.append(S[i])
                count = 1
            else:
                count += 1
        counts.append(count)
        return chars, counts
