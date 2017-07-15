# Time: O(logn)
# Space: O(1)
"""
Binary search
Key: Go left or right?

Step1: which part is mid in?
Target in Part 1 or Part 2
    arr[mid] > arr[start] -> arr[mid] in Part 1
    arr[mid] < arr[start] -> arr[mid] in Part 2

Step 2: which part may target be in?
    target >= arr[start] and target < arr[mid] -> target in Part 1
    target < arr[end] and target > arr[mid] -> target in Part 2
"""
class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        start = 0
        end = len(nums) - 1

        if start == end:
            if nums[start] == target:
                return 0
            else:
                return -1

        while start + 1 < end:
            mid = start + (end - start) // 2
            
            if nums[mid] == target:
                return mid
            # step 1: locate nums[mid]
            if nums[mid] > nums[start]:
                # step 2: locate target
                if target >= nums[start] and target < nums[mid]: # mid in 1 and target in 1
                    end = mid
                else: # mid in 1 and target in 2
                    start = mid
            else: # elif: nums[mid] < nums[start]
                if target < nums[end] and target > nums[mid]: # mid in 2 and target in 2
                    start = mid
                else: # mid in 2 and target in 1
                    end = mid
            # else: # follow up: what if duplicates?
            #     start += 1

            if nums[start] == target:
                return start
            if nums[end] == target:
                return end

        return -1


if __name__ == "__main__":
    new = Solution()
    print(new.search([6, 7, 8, 0, 1, 3, 5], 1))
    print(new.search([1], 1))
    print(new.search([1], 0))