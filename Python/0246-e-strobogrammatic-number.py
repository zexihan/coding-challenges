class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        i = 0
        j= len(num) - 1
        while i <= j:
            if num[i] == num[j] and num[i] not in ['0','1','8']:
                return False
            elif num[i] != num[j] and (num[i] not in ['6','9'] or num[j] not in ['6','9']):
                return False
            i += 1
            j -= 1
        return True