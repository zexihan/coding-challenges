"""
ranger
Time: O(n)
Space: O(1)
"""
class Solution_1:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        ranger = 1
        while x / ranger >= 10:
            ranger *= 10

        while x:
            left = x // ranger
            right = x % 10
            if left != right:
                return False
            
            x = (x % ranger) // 10
            ranger /= 100
        return True

"""
two pointers
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        x = str(x)
        i, j = 0, len(x) - 1
        while i <= j:
            if x[i] != x[j]:
                return False
            i += 1
            j -= 1
        return True