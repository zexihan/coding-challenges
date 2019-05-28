class Solution_1:
    def canPermutePalindrome(self, s: str) -> bool:
        count = 0  # the number of characters with odd number of occurences
        i = 0
        while i < 128 and count <= 1:
            ct = 0
            for j in range(len(s)):
                if s[j] == chr(i):
                    ct += 1
            count += ct % 2
            i += 1
        return count <= 1


class Solution_2:
    def canPermutePalindrome(self, s: str) -> bool:
        map = {}
        for i in range(len(s)):
            map[s[i]] = map.get(s[i], 0) + 1
        count = 0
        for value in map.values():
            count += value % 2
        return count <= 1


class Solution_3:
    def canPermutePalindrome(self, s: str) -> bool:
        map = [0] * 128
        for i in range(len(s)):
            map[ord(s[i])] += 1
        count = 0
        for value in map:
            count += value % 2
        return count <= 1


class Solution_4:
    def canPermutePalindrome(self, s: str) -> bool:
        map = [0] * 128
        count = 0
        for i in range(len(s)):
            map[ord(s[i])] += 1
            if map[ord(s[i])] % 2 == 0:
                count -= 1
            else:
                count += 1
        return count <= 1


class Solution_5:
    def canPermutePalindrome(self, s: str) -> bool:
        sset = set()
        for i in range(len(s)):
            if s[i] in sset:
                sset.discard(s[i])
            else:
                sset.add(s[i])
        return len(sset) <= 1
