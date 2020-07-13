// DP
class Solution {
public:
    int coinChange(vector<int>& coins, int amount) {
        vector<int> f(amount + 1, amount + 1);
        f[0] = 0;
        for (int i = 1; i< amount + 1; i++) {
            for (int k : coins) {
                if (i >= k && f[i - k] != amount + 1) {
                    f[i] = min(f[i], f[i - k] + 1);
                }
            }
        }
        return f[amount] != amount + 1 ? f[amount] : -1;
    }
};