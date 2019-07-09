"""
Binary Search
Time: O(log(m+n))
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        if total % 2 == 0:
            return (self.findKth(nums1, 0, nums2, 0, total // 2) +
                    self.findKth(nums1, 0, nums2, 0, total // 2 + 1)) / 2
        else:
            return self.findKth(nums1, 0, nums2, 0, total // 2 + 1)

    # k is not index, k >= 1
    def findKth(self, nums1, idx1, nums2, idx2, k):
        # nums1 is empty
        if idx1 >= len(nums1):
            return nums2[idx2 + k - 1]
        # nums2 is empty
        if idx2 >= len(nums2):
            return nums1[idx1 + k - 1]

        if k == 1:
            return min(nums1[idx1], nums2[idx2])

        key1 = float('inf')
        key2 = float('inf')

        if idx1 + k // 2 - 1 < len(nums1):
            key1 = nums1[idx1 + k // 2 - 1]

        if idx2 + k // 2 - 1 < len(nums2):
            key2 = nums2[idx2 + k // 2 - 1]

        if key1 < key2:
            return self.findKth(nums1, idx1 + k // 2, nums2, idx2, k - k // 2)
        else:
            return self.findKth(nums1, idx1, nums2, idx2 + k // 2, k - k // 2)
