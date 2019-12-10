"""
Hash Table
"""
import collections
class Solution_1:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        
        count = collections.defaultdict(int)
        for m in hand:
            count[m] += 1
                
        while count:
            m = min(count.keys())
            mCnt = count[m]
            for k in range(m, m + W):
                v = count[k]
                if v < mCnt: 
                    return False
                if v == mCnt:
                    del count[k]
                else:
                    count[k] = v - mCnt
        return True

"""
Sorting
"""
class Solution_2:
    def isNStraightHand(self, hand: List[int], W: int) -> bool:
        if len(hand) % W != 0:
            return False
        hand.sort()
        while hand:
            base = hand[0]
            for i in range(W):
                if base + i in hand:
                    hand.remove(base+i)
                else:
                    return False
        return True
