"""
Time:
Space:
"""
class Solution:

    def __init__(self, size: int) -> None:
        self.size = size
        self.list = []
        

    def next(self, val: int) -> int:
        self.list.append(val)
        if len(self.list) < self.size:
            return sum(self.list) / len(self.list)
        else:
            sumNumbers=0
            for i in range(self.size):
                sumNumbers += self.list[-i-1]
            return sumNumbers / self.size