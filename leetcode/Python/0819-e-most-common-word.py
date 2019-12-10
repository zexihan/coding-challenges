import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.replace(',', ' ')
        count = collections.Counter([word.strip("!?',;.")
                                     for word in paragraph.lower().split()])
        bannSet = set(banned)
        res = ""
        resCnt = 0
        for word, cnt in count.items():
            if cnt > resCnt and word not in bannSet:
                resCnt = cnt
                res = word
        return res
