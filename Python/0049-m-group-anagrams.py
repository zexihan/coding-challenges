"""
Time: O(n)
Space: O(1)
"""
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = collections.defaultdict(list)
        for s in strs:
            ss = "".join(sorted(s))
            map[ss].append(s)
        return list(map.values())