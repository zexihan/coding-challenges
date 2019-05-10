"""
复习一下整数除法，用长除式的时候，不断地得到当前除法的商和余数，然后给余数部分补零继续做除法。
当我们遇到了一个余数，而且这个余数在前面已经出现过了，那么就是出现了循环了。

所以，我们需要一个dict来保存出现过的余数，以及得出这个余数时候，结果出现的位置。所以再次得到这
个余数的时候，就查出来了上次出现了的位置，中间这一段就是循环小数部分。

另外特别注意的是，这个题目支持负数除法，所以最好的方法全部转化为正整数的除法，先判断结果的符号，
然后把结果变成正数。
"""
class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        d = dict()
        div, mod = self.divmod(numerator, denominator)
        if mod == 0:
            return str(div)
        ans = "-" if (numerator > 0) ^ (denominator > 0) else ""
        div, mod, denominator = abs(div), abs(mod), abs(denominator)
        ans += str(div) + "."
        d[mod] = len(ans)
        while mod:
            mod *= 10
            div, mod = self.divmod(mod, denominator)
            ans += str(div)
            if mod in d:
                index = d[mod]
                ans = ans[:index] + "(" + ans[index:] + ")"
                break
            else:
                d[mod] = len(ans)
        return ans

    def divmod(self, a, b):
        q = int(a / b)
        r = a - q * b
        return (q, r)
