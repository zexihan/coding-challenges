class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []
        result = []
        temp = ['0'] * (len(s) + 3)
        self.dfs(result, s, temp, 0, 0)
        return result
    
    def dfs(self, result, s, temp, sI, eI):
        if eI == 4:
            if sI == len(s):
                result.append(''.join(temp))
            return
        num = 0
        for i in range(sI, len(s)):
            if i < sI + 3:
                if s[sI] == '0' and i != sI:
                    break
                num = num * 10 + ord(s[i]) - ord('0')
                if num > 255:
                    break
                temp[i + eI] = s[i]
                if eI != 3:
                    temp[i + eI + 1] = '.'
                self.dfs(result, s, temp, i + 1, eI + 1)
