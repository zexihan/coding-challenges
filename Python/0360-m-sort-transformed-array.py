class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        if not nums:
            return []
        i, j = 0, len(nums) - 1
        res = []
        f = lambda x: a * x**2 + b * x + c
        while i <= j:
            v1, v2 = f(nums[i]), f(nums[j])
            if a > 0:
                if v1 > v2:
                    res.append(v1)
                    i += 1
                else:
                    res.append(v2)
                    j -= 1
            else:
                if v1 > v2:
                    res.append(v2)
                    j -= 1
                else:
                    res.append(v1)
                    i += 1
        return res[::-1] if a > 0 else res