class Solution_1:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split(".")
        nums2 = version2.split(".")
        n = max(len(nums1), len(nums2))
        
        nums1 += [0] * (n - len(nums1))
        nums2 += [0] * (n - len(nums2))
        
        for i in range(n):
            num1 = int(nums1[i])
            num2 = int(nums2[i])
            if num1 > num2:
                return 1
            elif num1 < num2:
                return -1
        return 0

# Recursion
class Solution_2:
    def compareVersion(self, version1: str, version2: str) -> int:
        if version1 == version2:
            return 0
        
        ind1 = version1.find(".")
        ind2 = version2.find(".")
        part1 = version1[0:ind1] if ind1 != -1 else version1
        part2 = version2[0:ind2] if ind2 != -1 else version2

        if int(part1) == int(part2):
            remain1 = version1[len(
                part1) + 1:] if version1[len(part1) + 1:] != "" else "0"
            remain2 = version2[len(
                part2) + 1:] if version2[len(part2) + 1:] != "" else "0"
            return self.compareVersion(remain1, remain2)
        else:
            return 1 if int(part1) > int(part2) else -1
