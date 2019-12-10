"""
Stack
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):   
            if tokens[i] not in ["+", "-", "*", "/"]:
                stack.append(int(tokens[i]))
                print(stack)
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if tokens[i] == "+":
                    stack.append(op2 + op1)
                elif tokens[i] == "-":
                    stack.append(op2 - op1)
                elif tokens[i] == "*":
                    stack.append(op2 * op1)
                else:
                    stack.append(int(op2 / op1))
                print(stack)
        return stack[0]


"""
Same idea as above, Python version with map and lambda
Time: O(n)
Space: O(n)
"""
import operator
class Solution_2:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        opt = {'+': lambda x, y: int(x) + int(y), 
              '-': lambda x, y: int(x) - int(y), 
              '*': lambda x, y: int(x) * int(y), 
              '/': lambda x, y: int(operator.truediv(int(x), int(y)))}
        for i in tokens:
            if i not in opt:
                stack.append(i)
            else:
                y, x = stack.pop(), stack.pop()
                stack.append(opt[i](x, y))
        return int(stack[-1])