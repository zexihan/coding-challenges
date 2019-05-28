# Time: O(n)
# Space: O(1)
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for i in nums:
            res ^= i
        return res

if __name__ == "__main__":
    new = Solution()
    print(new.singleNumber([4,2,1,1,7,4,2])) # 7