// a/b = e^(ln(a))/e^(ln(b)) = e^(ln(a)-ln(b))
class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend==0) return 0;
        if (divisor==0) return INT_MAX;
        long long res=double(exp(log(fabs(dividend))-log(fabs(divisor))));
        if ((dividend<0)^(divisor<0)) res=-res;
        if (res>INT_MAX) res=INT_MAX;
        return res;
    }
};

class Solution {
public:
    int divide(int dividend, int divisor) {
        if (dividend == INT_MIN && divisor == -1)
            return INT_MAX;
        
        int negatives = 2;
        if (dividend > 0) {
            negatives--;
            dividend = -dividend;
        }
        if (divisor > 0) {
            negatives--;
            divisor = -divisor;
        }
        
        int quotient = 0;
        while (dividend - divisor <= 0) {
            quotient--;
            dividend -= divisor;
        }
        
        if (negatives != 1)
            return -quotient;
        return quotient;
    }
};