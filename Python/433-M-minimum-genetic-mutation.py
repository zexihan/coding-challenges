"""
refer to 127
bfs
Time: O(NL)
Space: O(N)
N: the num of word in bank
L: the length of gene
"""
import collections
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        q = collections.deque()
        q.append((start, 0))
        bankSet = set(bank)
        while q:
            gene, step = q.popleft()
            if gene == end:
                return step
            for i in range(len(gene)):
                for x in "ACGT":
                    newGene = gene[:i] + x + gene[i+1:]
                    if newGene in bankSet and newGene != gene:
                        q.append((newGene, step + 1))
                        bankSet.remove(newGene)
        return -1