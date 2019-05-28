class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = 0
        tail = len(s) - 1
        while tail >= 0 and s[tail] == " ":
            tail -= 1
        while tail >= 0 and s[tail] != " ":
            length += 1
            tail -= 1
        return length

if __name__ == "__main__":
    new = Solution()
    print(new.lengthOfLastWord("Hello World"))