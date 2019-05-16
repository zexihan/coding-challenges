import collections
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.set = set(dictionary)
        self.dict = collections.defaultdict(int)
        for word in self.set:
            self.dict[self.toAbbr(word)] += 1

    def isUnique(self, word: str) -> bool:
        abbr = self.toAbbr(word)
        if abbr not in self.dict:
            return True
        elif self.dict[abbr] == 1 and word in self.set:
            return True
        else: return False
    
    def toAbbr(self, s):
        n = len(s)
        if n <= 2:
            return s
        return s[0] + str(len(s) - 2) + s[n - 1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)