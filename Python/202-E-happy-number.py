# Time: O(1) (O(810))
class Solution_1(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        cache = []
        while n not in cache:
            cache.append(n)
            result = 0
            while n:
                result += (n % 10)**2
                n //= 10
            if result == 1:
                    return True
            n = result
        return False

# Space: O(1)
# Floyd Cycle detection algorithm
class Solution_2(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        slow = fast = n
        while True:
            slow = self.transform(slow)
            fast = self.transform(fast)
            fast = self.transform(fast)
            if slow == fast:
                break
        if slow == 1: return True
        else: return False

    
    def transform(self, n):
        result = 0
        while n:
            result += (n % 10)**2
            n /= 10
        return result

if __name__ == "__main__":
    new = Solution_1()
    print(new.isHappy(1))