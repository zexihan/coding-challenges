# Time:
# Space:
class Solution(object):
    
    dict = {} # <number, frequency>
    list = [] # for iteration to find

    def add(self, number):
        self.list.append(number)
        frequency=number in self.dict.keys()
        if frequency == 0:
            self.dict[number]=1
        else:
            self.dict[number]=frequency+1
        print(self.dict)
        print(self.list)

    def find(self, value):
        for curKey in self.list:
            target=value-curKey
            if target in self.dict.keys():
                if (curKey != target) or (curKey==target and self.dict[target]>=2):
                    return True
        return False


if __name__ == '__main__':
    new = Solution()
    new.add(3)
    new.add(1)
    print(new.find(4))
    new.add(2)
    new.add(1)
    print(new.find(6))
    print(new.find(2))
