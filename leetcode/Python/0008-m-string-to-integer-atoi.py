class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.strip()
        if str == "":
            return 0
        i = 0
        sign = 1
        res = 0
        length = len(str)
        MaxInt = (1 << 31) - 1
        if str[i] == '+':
            i += 1
        elif str[i] == '-':
            i += 1
            sign = -1

        for i in range(i, length):
            if str[i] < '0' or str[i] > '9':
                break
            res = res * 10 + int(str[i])
            if res > MaxInt:
                break

        res *= sign
        if res >= MaxInt:
            return MaxInt
        if res < MaxInt * (-1):
            return MaxInt * (-1) - 1
        return res
