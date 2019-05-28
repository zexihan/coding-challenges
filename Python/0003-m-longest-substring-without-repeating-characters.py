"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        map = {}
        for i in range(len(s)):
            if s[i] in map and map[s[i]] >= left:
                left = map[s[i]] + 1
            map[s[i]] = i
            res = max(res, i - left + 1)
        return res

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb"))