"""
BFS
"""
import collections
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        start = '0000'
        if start == target:
            return 0

        deadset = set(deadends)
        if start in deadset:
            return -1

        q = collections.deque()
        visited = set()

        q.append(start)
        visited.add(start)

        dist = 0
        while q:
            dist += 1
            size = len(q)
            for i in range(size):
                cur = q.popleft()
                for k in range(4):
                    next = cur[:k] + str((ord(cur[k]) -
                                          ord('0') - 1 + 10) % 10) + cur[k+1:]
                    if next == target:
                        return dist
                    if next not in visited and next not in deadset:
                        q.append(next)
                        visited.add(next)

                    next = cur[:k] + str((ord(cur[k]) -
                                          ord('0') + 1 + 10) % 10) + cur[k+1:]
                    if next == target:
                        return dist
                    if next not in visited and next not in deadset:
                        q.append(next)
                        visited.add(next)

        return -1