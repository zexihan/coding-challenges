/*
 * Binary Search
 */
class Solution {
    public int mySqrt(int x) {
        if (x < 0)
            throw new IllegalArgumentException();
        else if (x <= 1)
            return x;

        int start = 1, end = x;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (mid == x / mid)
                return mid;

            else if (mid < x / mid)
                start = mid;
            else
                end = mid;
        }

        if (end > x / end)
            return start;
        return end;
    }
}