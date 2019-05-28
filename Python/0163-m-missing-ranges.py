class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        res = []
        if len(nums) == 0:
            res.append(self.getRange(lower, upper))
            return res
        pre = lower - 1
        for cur in nums:
            if pre != cur and pre + 1 != cur:
                res.append(self.getRange(pre + 1, cur - 1))
            pre = cur
        if nums[-1] < upper:
            res.append(self.getRange(nums[-1] + 1, upper))
        return res

    def getRange(self, lower, upper):
        if lower == upper:
            return "{}".format(lower)
        else:
            return "{}->{}".format(lower, upper)
