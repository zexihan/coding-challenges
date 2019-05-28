"""
DFS
Time: O(n)
"""
class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        visited = [False for i in range(n)]
        for i in range(n):
            if visited[i]:
                continue
            visited[i] = True
            dic = set()
            cur = i
            while True:
                next = (cur + nums[cur]) % n
                if next == cur or nums[next] * nums[cur] < 0:
                    break
                if next in dic:
                    return True
                dic.add(cur)
                cur = next
                visited[next] = True
        return False
