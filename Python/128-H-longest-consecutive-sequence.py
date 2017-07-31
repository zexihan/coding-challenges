# Time: O(nlogn)
# Space: O(1)
"""
Primitive idea:
Sorting method
"""
class Solution_1(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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


# Time: O(n)
# Space: O(n)
"""
Set method
Put nums into set
For each element of nums, find its lower and upper bound
"""
class Solution_2(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxCount = 0
        numSet = set(nums)

        for n in nums:
            curr = n
            count = 0
            # check upper bound
            while curr in numSet:
                numSet.remove(curr)
                curr += 1
                count += 1
                
            # check lower bound
            curr = n - 1
            while curr in numSet:
                numSet.remove(curr)
                curr -= 1
                count += 1
            
            maxCount = max(count, maxCount)
        
        return maxCount
            

if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(new_1.longestConsecutive([100, 4, 101, 1, 3, 2, 102, 7, 99, 12, 98]))
    print(new_1.longestConsecutive([]))
    print(new_2.longestConsecutive([100, 4, 200, 1, 3, 2]))
    print(new_2.longestConsecutive([100, 4, 101, 1, 3, 2, 102, 7, 99, 12, 98]))
    print(new_2.longestConsecutive([]))