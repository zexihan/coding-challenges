# Time: O(k + nlogn) 42ms
# Space: O(1)
"""
Primitive idea: sort and count
Sort -> Merge/Quick Sort O(nlogn)
"""
class Solution_1(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return sorted(nums, reverse=True)[k - 1]

# Time: O((n-k)logk + k) 72ms
# Space: O(k)
"""
Heap

Only need to sort k largest elements
Store k sorted elements: heap

Always store the largest k elems
Pop the smallest one
First: heapify -> O(k)
Pop/Push an element: logk
Last: Pop the top elem

"""
import heapq
class Solution_2(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # maintain a min heap with size k
        minHeap = []
        heapq.heapify(minHeap)
        # 1. add first k elems
        for i in range(k):
            heapq.heappush(minHeap, nums[i])
        # 2. add rest elems
        for i in range(k, len(nums)):
            if nums[i] > minHeap[0]:
                heapq.heappop(minHeap)
                heapq.heappush(minHeap, nums[i])
        return heapq.heappop(minHeap)





if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_1()
    print(new_1.findKthLargest([3,2,1,5,6,4], 2)) # 5
    print(new_2.findKthLargest([3,2,1,5,6,4], 2)) # 5