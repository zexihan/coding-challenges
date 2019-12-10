class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        pos1 = -1
        pos2 = -1
        dist = len(words)
        for i in range(len(words)):
            if words[i] == word1:
                pos1 = i
            elif words[i] == word2:
                pos2 = i
        
            if pos1 != -1 and pos2 != -1:
                dist = min(dist ,abs(pos1 - pos2))
        return dist