# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        # find the only possible candidate
        k = 0
        for i in range(1, n):
            k = k if knows(i, k) else i
        
        # verify whether the candidate is the celebrity
        for i in range(n):
            if i != k and (knows(k, i) or not knows(i, k)):
                return -1
        return k