# Time: O(n)
# Space: O(n)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        left = 0
        dict = {}

        for i, ch in enumerate(s):
            if ch in dict and dict[ch] >= left:
                left = dict[ch] + 1
            dict[ch] = i
            res = max(res, i - left + 1)
        return res_

if __name__ == "__main__":
    new = Solution()
    print(new.lengthOfLongestSubstring("abcabcbb"))