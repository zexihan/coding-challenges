"""
Assume that the number is in [0,9], cannot pass all the testcases 
( -> offer into operator stack 
3 -> offer into number stack
) -> pop and calculate until a '(' is met 
+ -> 1. higher precedence met -> offer into stack
     2. lower precedence met -> calculate first
Time: O(n)
Space: O(n)
"""
import operator
class Solution:
    def calculate(self, s: str) -> int:
        s = list(s.replace(' ', ''))
        valStack = []
        opStack = []
        num = 0

        for i in range(len(s)):
            # case 1: '('
            if s[i] == '(':
                opStack.append(s[i])

            # case 2: ')'
            elif s[i] == ')':
                # pop and calculate with 1 operator and 2 numbers
                while opStack[len(opStack)-1] != '(':
                    valStack.append(self.cal(opStack.pop(), valStack.pop(), valStack.pop()))
                # pop '('
                opStack.pop()

            # case 3: operators other than parentheses
            elif s[i] in ['+', '-', '*', '/']:
                while opStack and self.isLowerThan(s[i], opStack[len(opStack)-1]):
                    valStack.append(self.cal(opStack.pop(), valStack.pop(), valStack.pop()))
                # offer current
                opStack.append(s[i])

            # case 4: number
            else:
                valStack.append(int(s[i]))
        # calculate all numbers rest in stack
        while opStack:
            valStack.append(self.cal(opStack.pop(), valStack.pop(), valStack.pop()))
        
        return valStack.pop()

    def cal(self, op, val2, val1):
        opt = {'+': lambda x, y: x + y, 
              '-': lambda x, y: x - y, 
              '*': lambda x, y: x * y, 
              '/': lambda x, y: int(operator.truediv(x, y))}
        return opt[op](val1, val2)

    def isLowerThan(self, cur, toPeek):
        return toPeek in ['*', '/'] and cur in ['+', '-']
