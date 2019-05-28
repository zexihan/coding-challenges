# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Time: O(nlogn)
# Space: O(n)

class Solution_1:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0

        tmp = []

        for inter in intervals:
            tmp.append((inter.start, True))
            tmp.append((inter.end, False))

        tmp = sorted(tmp, key=lambda v: (v[0], v[1]))

        n = 0
        max_num = 0
        for arr in tmp:
            if arr[1]:
                n += 1
            else:
                n -= 1
            max_num = max(n, max_num)
        return max_num

class Solution_2:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals: 
            return 0
        
        intervals = sorted(intervals, key = lambda x: x.start)
        heap = []
        heapq.heapify(heap)
        
        for interval in intervals:
            if heap and heap[0] <= interval.start: 
                heapq.heapreplace(heap, interval.end)
            else: 
                heapq.heappush(heap, interval.end)
        return len(heap)