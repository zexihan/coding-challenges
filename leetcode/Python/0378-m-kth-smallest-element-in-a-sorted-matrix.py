"""
Max Heap
Time: O(mnlogk)
Space: O(k)
"""
import heapq
class Solution_1:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        heapq.heapify(maxHeap)
        row, col = len(matrix), len(matrix[0])

        for i in range(row):
            for j in range(col):
                matrix[i][j] *= -1
                if len(maxHeap) < k:
                    heapq.heappush(maxHeap, matrix[i][j])
                else:
                    if maxHeap[0] >= matrix[i][j]:
                        break
                    else:
                        heapq.heapreplace(maxHeap, matrix[i][j])
        return -maxHeap[0]