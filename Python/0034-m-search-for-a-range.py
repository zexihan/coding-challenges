class Solution_1(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range = [len(nums), -1]
        self.search(nums, target, 0, len(nums) - 1, range)
        if range[0] > range[1]: range[0] = -1
        return range
    
    def search(self, nums, target, left, right, range):
        if left > right: return
        mid = left + (right - left) / 2
        if nums[mid] == target:
            if mid < range[0]:
                range[0] = mid
                self.search(nums, target, left, mid - 1, range)
            if mid > range[1]:
                range[1] = mid
                self.search(nums, target, mid + 1, right, range)
        elif nums[mid] < target:
            self.search(nums, target, mid + 1, right, range)
        else:
            self.search(nums, target, left, mid - 1, range)

class Solution_2(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        range = [-1, -1]
        i, j = 0, len(nums) - 1
        
        if len(nums) == 0 or nums is None:
            return range
        
        # search for the left one
        while i < j:
            mid = (i + j) / 2
            if nums[mid] < target:
                i = mid + 1
            else:
                j = mid
        if nums[i] != target:
            return range
        else:
            range[0] = i
        
        # search for the right one
        j = len(nums) - 1
        while i < j:
            mid = (i + j) / 2 + 1
            if nums[mid] > target:
                j = mid - 1
            else:
                i = mid
        range[1] = j
        return range