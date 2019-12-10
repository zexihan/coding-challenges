"""
DFS
Time: O(N x 4^n)
Space: O(N)
"""
class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        N = len(num)
        res = []
        def dfs(index, preOp, curOp, value, string):
            if index == N:
                if value == target and curOp == 0:
                    res.append("".join(string[1:]))
                return
            
            # extend the curOp by one digit
            curOp = curOp * 10 + int(num[index])
            strOp = str(curOp)
            
            # to avoid 1 + 05 or 1 * 05
            if curOp > 0:
                dfs(index + 1, preOp, curOp, value, string)
            
            # addition
            string.append('+')
            string.append(strOp)
            dfs(index + 1, curOp, 0, value + curOp, string)
            string.pop()
            string.pop()

            if string:
                # subtraction
                string.append('-')
                string.append(strOp)
                dfs(index + 1, -curOp, 0, value - curOp, string)
                string.pop()
                string.pop()
                
                # multiplication
                string.append('*')
                string.append(strOp)
                dfs(index + 1, curOp * preOp, 0, value - preOp + (curOp * preOp), string)
                string.pop()
                string.pop()


        dfs(0, 0, 0, 0, [])
        return res
    
    

