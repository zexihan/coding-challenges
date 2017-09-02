class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for i, num in enumerate(numbers):
            if target - num in map:
                return [map[target - num] + 1, i + 1]
            map[num] = i