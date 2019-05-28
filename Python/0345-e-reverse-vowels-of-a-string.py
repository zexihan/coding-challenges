# Time: O(n)
# Space: O(n)
class Solution_1:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = list(s)
        vowels = []
        for i in range(len(res)):
            if res[i] in ['a', 'o', 'e', 'i', 'u', 'A', 'O', 'E', 'I', 'U']:
                vowels.append((i, res[i]))
        for j in range(len(vowels)):
            res[vowels[j][0]] = vowels[len(vowels) - j - 1][1]
        return ''.join(res)

# Time: O(n)
# Space: O(1)
class Solution_2:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list('aeiouAEIOU'))
        s = list(s)
        front = 0
        end = len(s)-1
        while front < end:
            if s[front] in vowels:
                while not s[end] in vowels and front < end:
                    end -= 1
                s[front], s[end] = s[end], s[front]
                end -= 1
            front += 1

        return ''.join(s)
