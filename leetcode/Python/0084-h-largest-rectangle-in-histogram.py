"""
Stack
increasing stack
stack of index
cur > stack.peek() -> offer
cur <= stack.peek() -> continuously pop
Time: O(n)
Space: O(n)
"""
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(heights) + 1):
            # set curVal to the minimum value to guarantee the last elem to be put into stack
            curVal = 0 if i == len(heights) else heights[i]
            # 1. check whether curVal should be put into stack by comparing to peek
            while stack and heights[stack[-1]] >= curVal:
                height = heights[stack.pop()]
                # find left and right boundary from current rectangle
                leftBound = 0 if stack == [] else stack[-1] + 1
                rightBound = i
                res = max(res, height * (rightBound - leftBound))
            # 2. push the elem into the stack
            stack.append(i)
        return res
