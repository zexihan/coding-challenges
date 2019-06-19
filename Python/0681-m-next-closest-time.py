"""
String
Time: O(1)
Space: O(1)
"""
class Solution:
    def nextClosestTime(self, time: str) -> str:
        cur = 60 * int(time[:2]) + int(time[3:])
        allowed = {int(x) for x in time if x != ':'}
        while True:
            cur = (cur + 1) % (24 * 60)
            digits = [cur // 60 // 10, cur // 60 % 10, 
                      cur % 60 // 10, cur % 60 % 10]
            if all(digit in allowed for digit in digits):
                digits = [str(digit) for digit in digits]
                return digits[0] + digits[1] + ':' + digits[2] + digits[3]
