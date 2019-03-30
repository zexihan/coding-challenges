# The idea is to iterate over the numbers in secret and in guess and count all 
# bulls right away. For cows maintain an array that stores count of the number 
# appearances in secret and in guess. Increment cows when either number from 
# secret was already seen in guest or vice versa.
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bulls, cows = 0, 0
        numbers = [0] * 10
        for i in range(len(secret)):
            s = int(secret[i])
            g = int(guess[i])
            if s == g:
                bulls += 1
            else:
                if numbers[s] < 0:
                    cows += 1
                if numbers[g] > 0:
                    cows += 1
                numbers[s] += 1
                numbers[g] -= 1
        return str(bulls) + 'A' + str(cows) + 'B'
