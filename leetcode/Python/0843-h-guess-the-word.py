# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Master:
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

import random
class Solution:
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        n = 0
        while n < 6:
            guess = random.choice(wordlist)
            n = master.guess(guess)
            newWordlist = []
            for w in wordlist:
                if self.match(guess, w) == n:
                    newWordlist.append(w)
            wordlist = newWordlist
    
    def match(self, a, b):
        matches = 0
        for i in range(len(a)):
            if a[i] == b[i]:
                matches += 1
        return matches