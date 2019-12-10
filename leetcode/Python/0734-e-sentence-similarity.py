"""
Hash Table
Time: O(n)
Spa O(n)
"""
import collections
class Solution:
    def areSentencesSimilar(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False

        hash = collections.defaultdict(set)
        for pair in pairs:
            hash[pair[0]].add(pair[1])
            hash[pair[1]].add(pair[0])

        for i in range(len(words1)):
            if words1[i] != words2[i]:
                if words1[i] not in hash or words2[i] not in hash:
                    return False
                if words1[i] not in hash[words2[i]]:
                    return False
        return True