class Solution_1(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        return self.construct(res, n)
    
    def construct(self, res, n):
        alpha = "ZABCDEFGHIJKLMNOPQRSTUVWXYZ"
        a = n // 26
        b = n % 26
        res = alpha[b] + res
        if a == 0 or (a == 1 and b == 0):
            return res
        elif a > 1 and b == 0:
            return self.construct(res, a-1)
        return self.construct(res, a)
            
class Solution_2(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ""
        while n:
            n -= 1
            r = n % 26
            res = chr(ord("A") + r) + res
            n //= 26
        return res


if __name__ == "__main__":
    new = Solution_2()
    print(new.convertToTitle(79))