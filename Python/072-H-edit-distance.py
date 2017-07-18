# Recursion
class Solution_1(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
    
    def match(self, word1, word2, i, j):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if word1[i] == word2[j]:
            res = self.match(word1, word2, i + 1, j + 1)
        else:
            # case 1: insert
            insert = self.match(word1, word2, i, j + 1)
            # case 2: delete
            delete = self.match(word1, word2, i + 1, j)
            # case 3: replace
            replace = self.match(word1, word2, i + 1, j + 1)
            
            res = min(insert, delete, replace) + 1
        return res


# Time: O(len1 * len2)
# Space: O(len1 * len2)
# Memorized Search
class Solution_2(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

    def match(self, word1, word2, i, j, count):
        if i == len(word1):
            return len(word2) - j
        if j == len(word2):
            return len(word1) - i
        
        if count[i][j] != 0:
            return count[i][j]

        if word1[i] == word2[j]:
            res = self.match(word1, word2, i + 1, j + 1, count)
        else:
            # case 1: insert
            insert = self.match(word1, word2, i, j + 1, count)
            # case 2: delete
            delete = self.match(word1, word2, i + 1, j, count)
            # case 3: replace
            replace = self.match(word1, word2, i + 1, j + 1, count)
            
            res = min(insert, delete, replace) + 1
        
        count[i][j] = res
        
        return res

# Time: O(len1 * len2) 222ms
# Space: O(len1 * len2)
# Dynamic Programming
class Solution_3(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if len(word1) == 0 or len(word2) == 0:
            return len(word2) if len(word1) == 0 else len(word1)

        match = [[0 for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        # initialize base cases
        for i in range(len(word1) + 1):
            match[i][0] = i
        for j in range(len(word2) + 1):
            match[0][j] = j

        for i in range(len(word1)):
            for j in range(len(word2)):
                if word1[i] == word2[j]:
                    match[i + 1][j + 1] = match[i][j]
                else:
                    match[i + 1][j + 1] = min(match[i][j], match[i][j + 1], match[i + 1][j]) + 1
        # return the last one
        return match[len(word1)][len(word2)]

if __name__ == "__main__":
    new_3 = Solution_3()
    print(new_3.minDistance("head", "sad"))