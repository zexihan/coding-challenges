# Time:  O(nlogn)
# Space: O(n)
# return boolean
class Solution_1(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: boolean
        """
        
        if len(nums)<=1:
            return False

        nums = sorted(nums) # Time Complexity: O(nlogn)

        start = 0
        end = len(nums)-1

        # Move one pointer in each iteration
        while start < end:
            # Case 1: found
            if nums[start] + nums[end] == target:
                return True
            # Case 2: larger tha target: move end pointer
            elif nums[start] + nums[end] > target:
                end -= 1
            # Case 3: smaller than target: move start pointer
            else:
                start += 1

# Time:  O(n)
# Space: O(n)
# return index pairs
class Solution_2(object):
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # hash map
        if len(nums) <= 1:
            return False

        buff_dict = {}

        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                # key: target-nums[index]
                # value: index
                buff_dict[target - nums[i]] = i


if __name__ == '__main__':
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.twoSum([4, -3, 2, 11, 7, 15], 9))
    print(new_2.twoSum([4, -3, 2, 11, 7, 15], 9))