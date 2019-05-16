"""
naive
Time: O(n) - range sum query, O(1) - update query
"""
class NumArray_1:

    def __init__(self, nums: List[int]):
        self.nums = numsg

    def update(self, i: int, val: int) -> None:
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        return sum(self.nums[i : j + 1])

"""
sqrt decomposition - not accepted
Time complexity : O(n) - preprocessing, O(\sqrt{n}) - range sum query, O(1) - update query
["NumArray","sumRange","update","sumRange","sumRange","update","update","sumRange","sumRange","update","update"]
[[[-82,-39,-72,65,11,-56,-65,-39,27,97]],[5,6],[9,27],[2,3],[6,7],[1,-82],[3,-72],[3,7],[1,8],[5,13],[4,-67]]
"""
import math
class NumArray_2:

    def __init__(self, nums: List[int]):
        self.nums = nums
        l = math.sqrt(len(nums))
        if l == 0:
            self.length = 0
            self.b = []
        else:
            self.length = int(math.ceil(len(nums) / l))
            self.b = [0 for _ in range(self.length)]
            for i in range(len(nums)):
                self.b[i // self.length] += nums[i]
        

    def update(self, i: int, val: int) -> None:
        b_idx = i // self.length
        self.b[b_idx] = self.b[b_idx] - self.nums[i] + val
        self.nums[i] = val
        

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        startBlock = i // self.length
        endBlock = j // self.length
        if startBlock == endBlock:
            for k in range(i, j + 1):
                sum += self.nums[k]
        else:
            for k in range(i, (startBlock + 1) * self.length):
                sum += self.nums[k]
            for k in range(startBlock + 1, endBlock - 1):
                sum += self.b[k]
            for k in range(endBlock * self.length, j + 1):
                sum += self.nums[k]
        return sum


"""
segment tree
Time: O(logn) - range sum query, O(logn) - update query
"""
class NumArray_3:

    def __init__(self, nums: List[int]):
        self.nums = nums
        if len(nums) > 0:
            self.n = len(nums)
            self.tree = [0 for i in range(self.n * 2)]
            self.buildTree(nums)

    def buildTree(self, nums):
        i, j = self.n, 0
        while i < 2 * self.n:
            self.tree[i] = self.nums[j]
            i += 1
            j += 1
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, i: int, val: int) -> None:
        i += self.n
        self.tree[i] = val
        while i > 0:
            left = i
            right = i
            if i % 2 == 0:
                right = i + 1
            else:
                left = i - 1
            # parent is updated after child is updated
            self.tree[i // 2] = self.tree[left] + self.tree[right]
            i //= 2

    def sumRange(self, i: int, j: int) -> int:
        # get leaf with value 'l'
        i += self.n
        # get lead with value 'r'
        j += self.n
        sum = 0
        while i <= j:
            if i % 2 == 1:
                sum += self.tree[i]
                i += 1
            if j % 2 == 0:
                sum += self.tree[j]
                j -= 1
            i //= 2
            j //= 2
        return sum


"""
binary indexed tree / fenwick tree
"""
class NumArray_4:

    def __init__(self, nums: List[int]):
        self.nums = nums
        l = math.sqrt(len(nums))
        if l == 0:
            self.length = 0
            self.b = []
        else:
            self.length = int(math.ceil(len(nums) / l))
            self.b = [0 for _ in range(self.length)]
            for i in range(len(nums)):
                self.b[i // self.length] += nums[i]

    def update(self, i: int, val: int) -> None:
        b_idx = i // self.length
        self.b[b_idx] = self.b[b_idx] - self.nums[i] + val
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        sum = 0
        startBlock = i // self.length
        endBlock = j // self.length
        if startBlock == endBlock:
            for k in range(i, j + 1):
                sum += self.nums[k]
        else:
            for k in range(i, (startBlock + 1) * self.length):
                sum += self.nums[k]
            for k in range(startBlock + 1, endBlock - 1):
                sum += self.b[k]
            for k in range(endBlock * self.length, j + 1):
                sum += self.nums[k]
        return sum


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
