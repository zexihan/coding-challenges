class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_s = {}
        map_t = {}
        for chr in list(s):
            map_s[chr] = map_s.get(chr,0) + 1
        for chr in list(t):
            map_t[chr] = map_t.get(chr,0) + 1
        return map_s == map_t