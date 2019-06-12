"""
Sliding Window
Equivalently, we want the longest subarray with at most two "types" (values of tree[i]).
Time: O(n)
Space: O(n)
"""
import collections
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        res, i = 0, 0
        count = collections.defaultdict(int)
        for j in range(len(tree)):
            count[tree[j]] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    del count[tree[i]]
                i += 1
            res = max(res, j - i + 1)
        return res
