import collections
class Solution:
    def slidingPuzzle(self, board) -> int:
        start = ""
        for i in range(2):
            for j in range(3):
                start += str(board[i][j])
        if start == "123450":
            return 0
        
        res = 0
        q = collections.deque()
        q.append((start, start.find('0')))
        visited = set()
        self.flag = False
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        while q:
            size = len(q)
            for i in range(size):
                state, zidx = q.popleft()
                cx, cy = zidx // 3, zidx % 3
                for j in range(4):
                    self.bfs(state, zidx, cx + dx[j], cy + dy[j], visited, q)
                    if self.flag == True:
                        return res + 1
            res += 1
        return -1

    def bfs(self, s, zidx, x, y, visited, q):
        if x < 0 or x >= 2 or y < 0 or y >= 3:
            return
        nzidx = x * 3 + y
        s = s[:zidx] + s[nzidx] + s[zidx + 1:]
        s = s[:nzidx] + '0' + s[nzidx + 1:]
        if s == "123450":
            self.flag = True
            return
        if s not in visited:
            visited.add(s)
            q.append((s, nzidx))

if __name__ == '__main__':
    print(Solution().slidingPuzzle([[3, 2, 4], [1, 5, 0]]))
