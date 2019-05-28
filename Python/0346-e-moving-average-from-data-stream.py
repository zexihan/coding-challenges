# Time:
# Space:
class Solution(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.list = []
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.list.append(val)
        if len(self.list) < self.size:
            return sum(self.list) / len(self.list)
        else:
            sumNumbers=0
            for i in range(self.size):
                sumNumbers += self.list[-i-1]
            return sumNumbers / self.size

if __name__ == '__main__':
    new = Solution(3)
    print(new.next(3))
    print(new.next(1))
    print(new.next(1))
    print(new.next(2))
