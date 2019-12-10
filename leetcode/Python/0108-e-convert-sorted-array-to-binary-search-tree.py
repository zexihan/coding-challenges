# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        head = self.helper(nums, 0, len(nums) - 1)
        return head
    
    def helper(self,nums, low, high):
        if low > high:
            return None
        mid = (low + high) / 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, low, mid - 1)
        node.right = self.helper(nums, mid + 1, high)
        return node