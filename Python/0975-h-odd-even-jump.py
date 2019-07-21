"""
DP + Binary search
Odd jump: find the smallest value greater than self (up)
Even jump: find the largest value less than self (down)

map<int, int> -> min index of the given value
dp[i][0]: can reach end starting with a up jump
dp[i][1]: can reach end starting with a down jump

Start from the (n - 2)th element
Find a valid up jump index j (lower bound)
Find a valid down jump index k (prev(upper bound))

dp[i][0] = dp[j][1] // next jump will be even (down)
dp[i][1] = dp[k][0] // next jump will be odd (up)

res = sum(dp[*][0])
Time: O(nlogn)
Space: O(n)
"""
class Solution:
    def oddEvenJumps(self, A: List[int]) -> int:
        N = len(A)

        def make(B):
            ans = [None] * N
            stack = []  # invariant: stack is decreasing
            for i in B:
                while stack and i > stack[-1]:
                    ans[stack.pop()] = i
                stack.append(i)
            return ans

        B = sorted(range(N), key=lambda i: A[i])
        oddnext = make(B)
        B.sort(key=lambda i: -A[i])
        evennext = make(B)

        odd = [False] * N
        even = [False] * N
        odd[N-1] = even[N-1] = True

        for i in range(N-2, -1, -1):
            if oddnext[i] is not None:
                odd[i] = even[oddnext[i]]
            if evennext[i] is not None:
                even[i] = odd[evennext[i]]

        return sum(odd)
