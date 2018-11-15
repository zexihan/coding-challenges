class Solution_1:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """     
        while num > 9:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num

class Solution_2:
    """
    :type num: int
    :rtype: int
    """ 
    def addDigits(self, num):
        if num == 0:
            return 0
        return (num - 1) % 9 + 1