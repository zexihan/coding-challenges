class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        
        while i < n:
            if nums[i] >= 0 and nums[i] < n and nums[nums[i]] != nums[i]:
                nums = self.swap(nums, i, nums[i])
            else:
                i += 1
        
        k = 1
        while k < n and nums[k] == k:
            k += 1
        
        if n == 0 or k < n:
            return k
        elif nums[0] == k: 
            return k + 1 
        else:
            return k
        
    def swap(self, nums: List[int], i: int, j: int) -> List[int]:
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
        return nums
