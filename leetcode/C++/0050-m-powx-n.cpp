// Time: O(logn)
// Space: O(logn)
class Solution {
public:
    double helper(double x, long long n) {
        if (n == 0)
            return 1.0;
        return n % 2 == 0 ? helper(x * x, n / 2) : x * helper(x * x, n / 2);
    }
    
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        return helper(x, N);
    }
};

// Iterative
// Time: O(logn)
// Space: O(1)
class Solution {
public:
    double myPow(double x, int n) {
        long long N = n;
        if (N < 0) {
            x = 1 / x;
            N = -N;
        }
        double res = 1;
        double cur_product = x;
        for (long long i = N; i; i /= 2) {
            if ((i % 2) == 1) {
                res = res * cur_product;
            }
            cur_product *= cur_product;
        }
        return res;
    }
};