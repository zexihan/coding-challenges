"""
Decreasing: visiting left node
Increasing: visiting right node
Time: O(n)
Space: O(n)
"""
class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        mi = -float('inf')
        stack = []
        for num in preorder:
            if num < mi:
                return False
            while stack and num > stack[-1]:
                mi = stack.pop()
            stack.append(num)
        return True
