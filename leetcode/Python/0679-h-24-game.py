"""
DFS
"""
class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        return self.compute(nums, 4)
    
    def compute(self, nums, n):
        if n == 1:
            if abs(nums[0] - 24) < 1e-9:
                return True
        
        for i in range(0, n):
            for j in range(i + 1, n):
                a, b = nums[i], nums[j]
                nums[j] = nums[n - 1]
                numsI = [a + b, a - b, b - a, a * b]
                if a != 0:
                    numsI.append(b / a)
                if b != 0: 
                    numsI.append(a / b)
                for num in numsI:
                    nums[i] = num
                    if self.compute(nums, n - 1):
                        return True
                nums[i] = a
                nums[j] = b
        return False
