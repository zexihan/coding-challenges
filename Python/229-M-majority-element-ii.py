"""
counter
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def majorityElement(self, nums: List[int]) -> List[int]:
        m = len(nums) // 3
        nset = set(nums)
        res = []
        for num in nset:
            if nums.count(num) > m:
                res.append(num)
        return res

"""
Moore Voting
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        N = len(nums)
        m, n, cm, cn = 0, 0, 0, 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
            elif cm == 0:
                m = num
                cm = 1
            elif cn == 0:
                n = num
                cn = 1
            else:
                cm -= 1
                cn -= 1
        cm, cn = 0, 0
        for num in nums:
            if num == m:
                cm += 1
            elif num == n:
                cn += 1
        if cm > N / 3:
            res.append(m)
        if cn > N / 3:
            res.append(n)
        return res
