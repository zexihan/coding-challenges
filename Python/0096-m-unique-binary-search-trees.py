"""
Recursion
Recursion rule: 
    count(3) = sum(count(i) * count(3 - i - 1)), i = 0 to 2
    count(n) = sum(count(i) * count(n - i - 1)), i = 0 to 2
Time: O(n!)
"""
class Solution_1:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        return self.count(n)

    def count(self, n):
        if n == 0 or n == 1:
            return 1
        sum = 0
        for i in range(n):
            sum += self.count(i) * self.count(n-i-1)
        return sum

"""
Recursion: Memorized Search
Time: O(n)
"""
class Solution_2:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        self.root = [0] * (n + 1)
        return self.count(n)

    def count(self, n):
        if n == 0 or n == 1:
            return 1
        if self.root[n] != 0:
            return self.root[n]
        sum = 0
        for i in range(n):
            sum += self.count(i) * self.count(n-i-1)
        self.root[n] = sum
        return sum
"""
DP
count(3) = sum(count(i) * count(3 - i - 1)), i = 0 to 2
count[3] = sum(count[i] * count[3 - i - 1]), i = 0 to 2
"""
class Solution_3:
    def numTrees(self, n: int) -> int:
        if n <= 0:
            return 0
        count = [0] * (n + 1)
        count[0] = 1

        for i in range(1, n + 1):
            for j in range(i):
                count[i] += count[j] * count[i - j - 1]
        return count[n]
