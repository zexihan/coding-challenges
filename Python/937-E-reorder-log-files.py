class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letterLogs = []
        numberLogs = []
        for l in logs:
            if l.split(" ")[-1].isdigit():
                numberLogs.append(l)
            else:
                letterLogs.append(l)
        return sorted(letterLogs, key=self.sortedKey) + numberLogs

    def sortedKey(self, s):
        i = s.index(" ")
        return (s[i+1:], s[:i])
