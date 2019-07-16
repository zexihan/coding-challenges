"""
Primitive idea
Sorting
Time: O(nlogn)
Space: O(n)
"""
class Solution_1:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums = sorted(nums)
        count = 1
        maxCount = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                count += 1
            else:
                count = 1

            maxCount = max(count, maxCount)

        return maxCount


"""
Set
Put nums into set
For each element of nums, find its lower and upper bound
Time: O(n)
Space: O(n)
"""
class Solution_2:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        for item in nums:
            numSet.add(item)

        res = 0
        for item in nums:
            if item in numSet:
                numSet.remove(item)

                l = item - 1
                r = item + 1
                while l in numSet:
                    numSet.remove(l)
                    l -= 1
                while r in numSet:
                    numSet.remove(r)
                    r += 1
                res = max(res, r - l - 1)
        return res
