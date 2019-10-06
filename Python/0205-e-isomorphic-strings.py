class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        map_dict = {}
        for i in range(len(s)):
            char_s, char_t = s[i], t[i]
            if char_s not in map_dict:
                if char_t not in list(map_dict.values()):
                    map_dict[char_s] = char_t
                else:
                    return False
            elif map_dict[char_s] == char_t:
                continue
            else:
                return False
        return True
