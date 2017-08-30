class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if strs is None:
            return [[]]
        map = {}
        for s in strs:
            ca = sorted(list(s))
            keyStr = "".join(ca)
            if keyStr not in map:
                map[keyStr] = []
            map[keyStr].append(s)
        return list(map.values())