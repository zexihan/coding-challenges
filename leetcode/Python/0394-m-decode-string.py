"""
stack
"""
class Solution:
    def decodeString(self, s: str) -> str:
        curNum = 0
        curStr = ""
        stack = []
        for c in s:
            if c .isdigit():
                curNum = curNum * 10 + int(c)
            elif c == "[":
                stack.append(curStr)
                stack.append(curNum)
                curStr = ""
                curNum = 0
            elif c == "]":
                preNum = stack.pop()
                preStr = stack.pop()
                curStr = preStr + preNum * curStr
            else:
                curStr += c
        return curStr
