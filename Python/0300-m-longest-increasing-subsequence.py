# Dynamic Programming, Binary Search
# F[1] = 1
# F[i] = max{1, F[j]+1 | aj<ai and j < i}

class Solution_1:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        dp=[1] * l
        for i in range(l):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution_2:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=[]
        for x in range(len(nums)):
            low = 0
            high = len(ans) - 1
            while low <= high:
                mid = (low + high) // 2 
                if ans[mid] < nums[x]: 
                    low = mid + 1            
                else:
                    high = mid - 1                              
            if low >= len(ans):                 
                ans.append(nums[x])
            else:                               
                ans[low] = nums[x]
        return len(ans)