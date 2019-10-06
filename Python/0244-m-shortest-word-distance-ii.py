class WordDistance:

    def __init__(self, words: List[str]):
        self.dict = {}
        for i, word in enumerate(words):
            if word not in self.dict:
                self.dict[word] = [i]
            else:
                self.dict[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1Indices = self.dict[word1]
        w2Indices = self.dict[word2]

        mini = float('inf')

        for i in w1Indices:
            for j in w2Indices:
                mini = min(mini, abs(j - i))
        return mini


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)
