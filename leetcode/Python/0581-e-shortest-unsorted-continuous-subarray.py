"""
Sorting
Time: O(nlogn)
Space: O(n)
"""
class Solution_1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        snums = sorted(nums)
        start = len(snums)
        end = 0
        for i in range(len(snums)):
            if snums[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
        return end - start + 1 if end - start >= 0 else 0

"""
Stack
Time: O(n)
Space: O(n)
"""
class Solution_2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        l = len(nums)
        r = 0
        for i in range(len(nums)):
            while len(stack) > 0 and nums[stack[-1]] > nums[i]:
                l = min(l, stack.pop())
            stack.append(i)

        stack = []
        for i in range(len(nums) - 1, -1, -1):
            while len(stack) > 0 and nums[stack[-1]] < nums[i]:
                r = max(r, stack.pop())
            stack.append(i)
        return r - l + 1 if r - l > 0 else 0

"""
4 loops
Time: O(n)
Space: O(1)
"""
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        def findMinMax(l, r):
            mi = float('inf')
            ma = float('-inf')
            for i in range(l, r + 1):
                if i == len(nums):
                    break
                mi = min(mi, nums[i])
                ma = max(ma, nums[i])

            return mi, ma

        if len(nums) < 2:
            return 0

        l, r = 0, len(nums) - 1

        while l < len(nums) - 1 and nums[l] <= nums[l + 1]:
            l += 1

        while r > 0 and nums[r] >= nums[r - 1]:
            r -= 1

        if l > r:
            return 0

        tempMin, tempMax = findMinMax(l, r + 1)

        while l > 0 and tempMin < nums[l - 1]:
            l -= 1

        while r < len(nums) - 1 and tempMax > nums[r + 1]:
            r += 1

        return r - l + 1
