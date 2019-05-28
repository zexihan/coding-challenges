# Max Heap
# Time: 279ms
import heapq
class Solution_1(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
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
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap, matrix[i][j])
        return -heapq.heappop(maxHeap)


# Pythonic
# Time: 82ms
class Solution_2(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        alist = sorted([ i for ele in matrix for i in ele ])
        return alist[k-1]


if __name__ == "__main__":
    new_1 = Solution_1()
    new_2 = Solution_2()
    print(new_1.kthSmallest([[1,  5,  9], [10, 11, 13], [12, 13, 15]], 8)) # 13
    print(new_2.kthSmallest([[1,  5,  9], [10, 11, 13], [12, 13, 15]], 8)) # 13


