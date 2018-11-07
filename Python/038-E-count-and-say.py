class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n < 1: return ''
        res = '1'
        for i in range(1,n):
            tmp = ''
            x = res[0]
            count = 1
            for c in res[1:]:
                if c == x:
                    count += 1
                else:
                    tmp += str(count) + x
                    x = c
                    count = 1
            res = tmp + str(count) + x
        return res