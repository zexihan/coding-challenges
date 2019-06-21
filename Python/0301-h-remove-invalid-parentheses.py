"""
BFS
Time: O(2^N)
Space: O(N)
"""
import collections
class Solution_1:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']
        q = collections.deque([s])
        res = []
        visited = set([s])
        found = False
        while q:
            cur = q.popleft()
            if self.isValidParentheses(cur):
                found = True
                res.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        nxt = cur[:i] + cur[i + 1:]
                        if nxt not in visited:
                            q.append(nxt)
                            visited.add(nxt)
        return res

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0:
                    return False
                cnt -= 1
        return cnt == 0 



"""
DFS + Pruning
Time: O(2^N)
Space: O(N)
"""
class Solution_2:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        if not s:
            return ['']
        left_rem, right_rem = 0, 0
        for c in s:
            if c == '(':
                left_rem += 1
            elif c == ')':
                if left_rem:
                    left_rem -= 1
                else:
                    right_rem += 1
        
        res = set()
        self.dfs(0, left_rem, right_rem, 0, '', s, res)
        return list(res)

    def dfs(self, index, left_rem, right_rem, left_pare, cur, s, res):
        if left_rem < 0 or right_rem < 0 or left_pare < 0: return
        if index == len(s):
            if left_rem == right_rem == left_pare == 0:
                res.add(cur)
            return
        
        if s[index] == '(':
            self.dfs(index + 1, left_rem - 1, right_rem, left_pare, cur, s, res)
            self.dfs(index + 1, left_rem, right_rem, left_pare + 1, cur + s[index], s, res)
        elif s[index] == ')':
            self.dfs(index + 1, left_rem, right_rem - 1, left_pare, cur, s, res)
            self.dfs(index + 1, left_rem, right_rem, left_pare - 1, cur + s[index], s, res)
        else:
            self.dfs(index + 1, left_rem, right_rem, left_pare, cur + s[index], s, res)
