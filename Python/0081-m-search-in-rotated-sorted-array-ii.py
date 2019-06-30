"""
Think about the worst case, e.g. [1, 1, 1, 1, 1, 0, 1, 1, 1]
Time: O(n)
Space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        for num in nums:
            if num == target:
                return True
        return False
