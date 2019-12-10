"""
iterative
这个题的思路是从把heater对house进行覆盖的思路转化成house距离
左右heater的最小距离。结果是所有最小距离的最大距离。
Time: O(n)
"""
class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        res = 0
        pos = 0
        heaters = [float('-inf')] + heaters + [float('inf')]
        for house in houses:
            while house >= heaters[pos]:
                pos += 1
            r = min(house - heaters[pos - 1], heaters[pos] - house)
            res = max(res, r)
        return res