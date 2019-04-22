"""
"..": pop
".": do nothing
"""
class Solution_1:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        res = ""
        while i < len(path):
            end = i + 1
            while end < len(path) and path[end] != "/":
                end += 1
            sub = path[i+1:end]
            if len(sub) > 0:
                if sub == "..":
                    if stack != []: stack.pop()
                elif sub != ".":
                    stack.append(sub)
            i = end
        if stack == []: return "/"
        for s in stack:
            res += "/" + s
        return res

class Solution_2:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for s in path.split("/"):
            if not s:
                continue
            elif s == ".":
                continue
            elif s == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(s)
        return "/" + "/".join(stack)
