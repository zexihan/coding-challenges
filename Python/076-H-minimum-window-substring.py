# Time:
# Space:
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # put all characters in t into map
        frequency = {}  # <char, index>
        chS = []

        for c in s:
            chS.append(c)

        for c in t:
            freq = frequency.get(c, 0)
            if freq == 0:
                frequency[c] = 1
            else:
                frequency[c] += 1

        left, right, count, minLen, startIndex = 0, 0, len(t), len(s), -1
        while right < len(chS):
            # move right to find a match
            freq = frequency.get(chS[right], None)
            if freq is not None:
                frequency[chS[right]] = freq - 1
                # in case of overmathch
                if freq > 0:
                    count -= 1
            right += 1
            # move left when a match is found
            while count == 0:
                if right - left <= minLen:
                    minLen = right - left
                    startIndex = left

                exist = frequency.get(chS[left], None)
                if exist is not None:
                    frequency[chS[left]] = exist + 1
                    # in case of overmathch
                    if exist == 0:
                        count += 1
                left += 1

        return s[startIndex:startIndex + minLen]

if __name__ == '__main__':
    new = Solution()
    print(new.minWindow("ADOBECODEBANC", "ABC"))
    print(new.minWindow("BXCDEBBDC", "DCB"))
    print(new.minWindow("ab", "ab"))

