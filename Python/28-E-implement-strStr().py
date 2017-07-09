# Time:
# Space:
class Solution_1(object):
    def strStr(self, haystack, needle):
        """
	    :type haystack: str
	    :type needle: str
	    :rtype: int
	    """
        i=0
        while i < len(haystack) - len(needle) + 1:
            m, n = i, 0
            while n < len(needle) and haystack[m] == needle[n]:
                m += 1
                n += 1
            if n == len(needle):
                return i
            i += 1
        return -1

# Time:
# Space:
class Solution_2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        len_h = len(haystack)
        len_n = len(needle)
        for i in range(0, len_h - len_n + 1):
            if needle == haystack[i:i+len_n]:
                return i
        return -1
