# Time: O(n)
# Space: O(n)
# Stack
class Solution_1(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
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

# Time: O(n)
# Space: O(n)
# Same idea as above, Python version with map and lambda:
import operator
class Solution_2(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
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


if __name__ == '__main__':
    new = Solution_1()
    print(new.evalRPN(["2", "1", "+", "3", "*"]))
    print(new.evalRPN(["4", "13", "5", "/", "+"]))
    print(new.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))