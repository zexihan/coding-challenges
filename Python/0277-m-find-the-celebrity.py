# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution():
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return -1
        if n == 1:
            return 0

        # 1. find a possible candidate who knows nobody else in his right hand
        candidate = 0
        for i in range(1, n):
            if knows(candidate, i):
                candidate = i
        # 2. check the candidate
        for i in range(n):
            # A. knows nobody in his left hand
            if i < candidate and knows(candidate, i):
                return -1
            # known by everyone else
            if not knows(i, candidate):
                return -1

        return candidate
