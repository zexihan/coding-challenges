"""
I: 1, V: 5, X: 10, L: 50, C: 100, D: 500, M: 1000
Time: O(n)
Space: O(1)
"""
class Solution(object):
   def intToRoman(self, num: int) -> str:
        vals = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        sybs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        roman = ''
        for idx, val in enumerate(vals):
            while num >= val:
                roman += sybs[idx]
                num -= vals[idx]
            if num == 0:
                return roman

if __name__ == "__main__":
    print(Solution().intToRoman(2478))  # MMCDLXXVIII
