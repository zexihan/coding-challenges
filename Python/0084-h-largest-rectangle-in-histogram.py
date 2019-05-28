# Time: O(n)
# Space: O(n)
"""
Key: find lower boundaties
Stack of index
cur > stack.peek() -> offer
cur <= stack.peek() -> continuously pop
"""
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        maxRec = 0
        for i in range(len(heights) + 1):
            # set curVal to the minimum value to guarantee the last elem to be put into stack
            curVal = 0 if i == len(heights) else heights[i]
            # 1. check whether curVal should be put into stack by comparing to peek
            while stack and heights[stack[-1]] >= curVal:
                height = heights[stack.pop()]
                # find left and right boundary from current rectangle
                leftBound = 0 if stack == [] else stack[-1] + 1
                rightBound = i
                maxRec = max(maxRec, height * (rightBound - leftBound))
            # 2. push the elem into the stack
            stack.append(i)
        return maxRec

if __name__ == '__main__':
    new = Solution()
    print(new.largestRectangleArea([2,1,5,6,2,3]))
    print(new.largestRectangleArea([1]))
