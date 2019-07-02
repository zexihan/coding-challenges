/*
 * Binary Search
 */
class Solution {
    public int arrangeCoins(int n) {
        int start = 1, end = n;
        int mid;
        long N = n;
        long cnt;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            cnt = (long) (mid + 1) * mid / 2;
            if (cnt <= N)
                start = mid;
            else
                end = mid;
        }
        
        if (start + start * start <= 2 * n)
            return start;
        return end;
    }
}