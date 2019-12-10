"""
Time: O(n)
Space: O(n)
"""
class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        if left[0] == '-':
            left = '0' + left
        if right[0] == '-':
            right = '0' + right
        left = left.replace('-', '+-')
        right = right.replace('-', '+-')
        left_x, left_val, right_x, right_val = 0, 0, 0, 0
        for num in left.split('+'):
            if 'x' in num:
                if num == 'x':
                    left_x += 1
                elif num == '-x':
                    left_x -= 1
                else:
                    left_x += int(num[:-1])
            else:
                left_val += int(num)
        for num in right.split('+'):
            if 'x' in num:
                if num == 'x':
                    right_x += 1
                elif num == '-x':
                    right_x -= 1
                else:
                    right_x += int(num[:-1])
            else:
                right_val += int(num)
        left_x -= right_x
        right_val -= left_val
        if left_x == 0 and right_val == 0:
            return "Infinite solutions"
        elif left_x == 0 and right_val != 0:
            return "No solution"
        else:
            return 'x=' + str(right_val // left_x)
        
