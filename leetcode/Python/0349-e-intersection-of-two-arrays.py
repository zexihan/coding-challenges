"""
Set
Time: O(m + n)
Space: O(m + n)
"""
class Solution_1:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set(nums1)
        set2 = set(nums2)

        if len(set1) < len(set2):
            return self.set_intersection(set1, set2)
        else:
            return self.set_intersection(set2, set1)

    def set_intersection(self, set1, set2):
        return [x for x in set1 if x in set2]

"""
Hash Table
Time: O(m + n)
Space: O(m + n)
"""
class Solution_2:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m, n = len(nums1), len(nums2)
        hash = {}
        if m > n:
            nums1, nums2 = nums2, nums1
        for num in nums1:
            hash[num] = True
        res = []
        for num in nums2:
            if num in hash and hash[num]:
                res.append(num)
                hash[num] = False
        return res

"""
Merge two sorted arrays
Time: O(nlogn + mlogm)
Space: O(1)
"""
class Solution_3:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        res = set()
        p1, p2 = 0, 0
        while p1 < len(nums1) and p2 < len(nums2):
            if nums1[p1] == nums2[p2]:
                res.add(nums1[p1])
                p1 += 1
                p2 += 1
            elif nums1[p1] < nums2[p2]:
                p1 += 1
            else:
                p2 += 1
        return list(res)

"""
Binary Search
Time: O(nlogn + mlogm)
Space: O(1)
"""
