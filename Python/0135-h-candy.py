"""
Two Pass
Time: O(n)
Space: O(n)
"""
class Solution_1:
    def candy(self, ratings: List[int]) -> int:
        left = [0 for i in range(len(ratings))]
        right = [0 for i in range(len(ratings))]
        left[0] = 1
        right[len(ratings) - 1] = 1
        
        # scan from left
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left[i] = left[i - 1] + 1
            else:
                left[i] = 1
        # scan from right
        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right[i] = right[i + 1] + 1
            else:
                right[i] = 1
        sum = 0
        for i in range(len(ratings)):
            sum += max(left[i], right[i])
        
        return sum


"""
One Pass
Time: O(n)
Space: O(1)
"""
class Solution_2:
    def candy(self, ratings: List[int]) -> int:
        sum = 1
        prev = 1
        down = 0
        for i in range(1, len(ratings)):
            if ratings[i] < ratings[i - 1]:
                down += 1
            else:
                # check descending sequence before
                if down > 0:
                    # step 1: add from 1 to down
                    sum += down * (down + 1) // 2 # 1+2+3+...+down
                    # step 2: add enough on prev
                    if down >= prev:
                        sum += down - prev + 1
                    prev = 1
                    down = 0
                prev = 1 if ratings[i] == ratings[i-1] else prev + 1
                sum += prev
        
        # check last descending sequence
        if down > 0:
            sum += down * (down + 1) // 2
            if down >= prev:
                sum += down - prev + 1
        
        return sum