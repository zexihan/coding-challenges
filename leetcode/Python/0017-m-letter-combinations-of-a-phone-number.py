from collections import deque
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits is None or len(digits) == 0:
            return []
        ans = deque()
        mapping = ["0", "1", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
        ans.append("")
        for i in range(len(digits)):
            x = int(digits[i])
            while len(ans[0]) == i:
                t = ans.popleft()
                for s in list(mapping[x]):
                    ans.append(t+s)
                    print(ans)
        return list(ans)