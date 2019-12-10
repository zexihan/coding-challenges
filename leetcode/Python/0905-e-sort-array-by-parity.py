"""
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for num in A:
            if num % 2 == 0:
                even.append(num)
            else:
                odd.append(num)
        return even + odd

"""
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        i, j = 0, len(A) - 1
        while i < j:
            if A[i] % 2 > A[j] % 2:
                A[i], A[j] = A[j], A[i]
            if A[i] % 2 == 0:
                i += 1
            if A[j] % 2 == 1:
                j -= 1
        return A