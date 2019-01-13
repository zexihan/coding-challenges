# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Time: O(nlogn)
# Space: O(1)

class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: bool
        """
        intervals.sort(key = lambda x: (x.start, x.end))
        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i+1].start:
                return False
        return True