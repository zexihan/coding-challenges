class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        n = len(A)
        m = len(B[0])
        t = len(A[0])
        C = [[0 for i in range(m)] for j in range(n)]

        col = []
        for i in range(t):
            col.append([])
            for j in range(m):
                if B[i][j] != 0:
                    col[i].append(j)

        for i in range(n):
            for k in range(t):
                if A[i][k] == 0:
                    continue
                for j in col[k]:
                    C[i][j] += A[i][k] * B[k][j]
        return C
