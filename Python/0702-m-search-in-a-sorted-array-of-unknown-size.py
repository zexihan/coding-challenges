"""
Binary Search
"""
class Solution:
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        index = 1
        while reader.get(index - 1) < target:
            index *= 2
        
        start, end = index // 2, index - 1
        while start + 1 < end:
            mid = start + (end - start) // 2
            if reader.get(mid) < target:
                start = mid
            else:
                end = mid
        
        if reader.get(start) == target:
            return start
        if reader.get(end) == target:
            return end
        
        return -1