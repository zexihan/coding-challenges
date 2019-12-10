"""
String
Time: O(n)
Space: O(1)
"""
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def backspace(s):
            skip = 0
            for x in s[::-1]:
                if x == '#':
                    skip += 1
                elif skip:
                    skip -= 1
                else:
                    yield x
        return list(backspace(S)) == list(backspace(T))
