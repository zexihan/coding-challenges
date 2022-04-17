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


// 使用倍增乘法逼近被除数，形如x/y=z的式子，计算z时，可以使用x >= y * z来逼近x，而z可以用2次幂来累加，进而来求出最大的z满足不等式。

// 例如：

// 59 / 3 = z
// ⇒ 59 = 3*z
// ⇒ x*z <= 59
// ⇒ 3 * (2^4 + 2^1 + 2^0 )
// ⇒ 3* ( 16 + 2 + 1)
// ⇒ 57
  
//  而 z =  (2^4 + 2^1 + 2^0 ) = 10011 (19)

// 按照下面写程序的思路，先得到z值的所有可能情况,
// z = {3*2^0,  3*2^1,  3*2^2,  3*2^3,  3*2^4} ,因为3 * (2^5) > 59了，所以往后的不计入在内。

// 计算z值（ans = 0）：
// 1, 59 - 3*2^4 = 11, 结果集ans = ans + 1<<4 = 16
// 2, 11 - 3*2^1 = 5, 结果集ans = ans + 1<< 1 = 16 + 2 = 18
// 3, 5 - 3*2^0 = 2, 结果集ans = ans + 1<< 0 = 16 + 2  + 1= 19(即，二进制10011)
// 4，2 < 3 ，循环终止，返回结果ans。
class Solution {
public:
    int divide(int dividend, int divisor) {
        // 考虑被除数为最小值的情况
        if (dividend == INT_MIN) {
            if (divisor == 1) {
                return INT_MIN;
            }
            if (divisor == -1) {
                return INT_MAX;
            }
        }
        // 考虑除数为最小值的情况
        if (divisor == INT_MIN) {
            return dividend == INT_MIN ? 1 : 0;
        }
        // 考虑被除数为 0 的情况
        if (dividend == 0) {
            return 0;
        }
        
        // 一般情况，使用类二分查找
        // 将所有的正数取相反数，这样就只需要考虑一种情况
        bool rev = false;
        if (dividend > 0) {
            dividend = -dividend;
            rev = !rev;
        }
        if (divisor > 0) {
            divisor = -divisor;
            rev = !rev;
        }

        vector<int> candidates = {divisor};
        // 注意溢出
        while (candidates.back() >= dividend - candidates.back()) {
            candidates.push_back(candidates.back() + candidates.back());
        }
        int ans = 0;
        for (int i = candidates.size() - 1; i >= 0; --i) {
            if (candidates[i] >= dividend) {
                ans += (1 << i);
                dividend -= candidates[i];
            }
        }

        return rev ? -ans : ans;
    }
};