class Solution {
public:
    int reverse(int x) {
        int res = 0;
        while (x != 0) {
            int tmp = x % 10; //取余 即123 % 10 = 3
            if (res > 214748364 || (res == 214748364 && tmp > 7)) //比最大值大
                return 0;
            if (res < -214748364 || (res == 214748364 && tmp < -8)) //比最小值小
                return 0;
            res = res * 10 + tmp; //重构数字
            x /= 10; //从后往前数字变小 即123 / 10 = 12
        }
        return res;
    }
};

/*
32位整数范围在 -2147483648 <= x <= 2147483647
通过取余和地板除完成数字的变小
*/
