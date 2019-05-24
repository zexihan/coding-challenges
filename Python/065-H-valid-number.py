class Solution:
    def isNumber(self, s: str) -> bool:
        if not s:
            return False

        i = 0
        s = s.strip()
        s += " "
        length = len(s) - 1

        if s[i] in ["+", "-"]:
            i += 1
        nDigit, nPoint = 0, 0
        while s[i].isdigit() or s[i] == ".":
            if s[i].isdigit():
                nDigit += 1
            if s[i] == ".":
                nPoint += 1
            i += 1
        if nDigit <= 0 or nPoint > 1:
            return False

        if s[i] == "e":
            i += 1
            if s[i] in ["+", "-"]:
                i += 1
            if i == length:
                return False
            while i < length:
                if not s[i].isdigit():
                    return False
                i += 1
        return i == length
