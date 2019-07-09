"""
Two Pointers
Time: O(n)
Space: O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            curtSum = numbers[left] + numbers[right]
            if curtSum < target:
                left += 1
            elif curtSum > target:
                right -= 1
            else:
                return [left + 1, right + 1]
