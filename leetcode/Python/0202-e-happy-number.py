"""
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def isHappy(self, n: int) -> bool:
        cache = set()
        while n != 1:
            s = 0
            while n:
                s += (n % 10) ** 2
                n //= 10
            if s in cache:
                return False
            cache.add(s)
            n = s
        return True

"""
Floyd Cycle detection algorithm
faster
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def isHappy(self, n: int) -> bool:
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
            n //= 10
        return result

if __name__ == "__main__":
    print(Solution_1().isHappy(1))
