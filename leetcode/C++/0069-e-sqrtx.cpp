class Solution {
public:
    int mySqrt(int x) {
        if (x < 0) return -1;
        else if (x <= 1) return x;

        int start = 1, end = x;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (mid == x / mid) return mid;
            if (mid < x / mid) 
                start = mid;
            else 
                end = mid;
        }
        return end > x / end ? start : end;
    }
};