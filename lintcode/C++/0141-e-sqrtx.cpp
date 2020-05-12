class Solution {
public:
    int sqrt(int x) {
        if (x < 0)
            return -1;
        if (x == 0)
            return x;
        long start = 0, end = x, mid;
        while (start + 1 < end) {
            mid = start + (end - start ) / 2;
            if (mid * mid == x)
                return mid;
            if (mid * mid > x) {
                end = mid;
                continue;
            }
            start = mid;
        }
        if (end * end <= x)
            return end;
        return start;
    }
};