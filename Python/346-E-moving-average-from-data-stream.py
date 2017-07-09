# Time:
# Space:
class Solution(object):

    list = []

    def __init__(self, window):
        self.window = window

    def next(self, number):
        self.list.append(number)
        if len(self.list)<self.window:
            return sum(self.list)/len(self.list)
        else:
            sumNumbers=0
            for i in range(self.window):
                sumNumbers += self.list[-i-1]
            return sumNumbers/self.window

if __name__ == '__main__':
    new = Solution(3)
    print(new.next(3))
    print(new.next(1))
    print(new.next(1))
    print(new.next(2))
