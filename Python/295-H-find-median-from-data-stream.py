from heapq import *
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minHeap = []
        self.maxHeap = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.minHeap) == len(self.maxHeap):
            heappush(self.maxHeap, -heappushpop(self.minHeap, num))
        else:
            heappush(self.minHeap, -heappushpop(self.maxHeap, -num))
        

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.minHeap) < len(self.maxHeap):
            return -1.0 * self.maxHeap[0]
        else:
            return (self.minHeap[0] - self.maxHeap[0]) / 2.0


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()