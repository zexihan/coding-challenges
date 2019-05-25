"""
iterative
"""
class Solution_1:
    def addDigits(self, num: int) -> int:
        while num > 9:
            s = 0
            while num:
                s += num % 10
                num //= 10
            num = s
        return num

"""
recursive
"""
class Solution_2:
    def addDigits(self, num: int) -> int:
        if len(str(num)) == 1:
            return num
        elif len(str(num)) == 2:
            return self.addDigits(int(str(num)[0]) + int(str(num)[1]))
        else:
            mid = len(str(num)) // 2
            return self.addDigits(self.addDigits(int(str(num)[:mid])) + self.addDigits(int(str(num)[mid:])))
