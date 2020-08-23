// DP
class Solution {
public:
    vector<int> countBits(int num) {
        vector<int> f(num + 1);
        f[0] = 0;
        for (int i = 1; i <= num; i++) {
            f[i] = (i % 2) + f[i >> 1];
        }
        return f;
    }
};