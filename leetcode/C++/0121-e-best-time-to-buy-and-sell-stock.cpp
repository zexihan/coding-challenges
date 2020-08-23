// DP
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        int res = 0;
        int minV = prices[0];
        for (int i = 1; i < n; ++i) {
            res = max(res, prices[i] - minV);
            minV = min(minV, prices[i]);
        }
        return res;
    }
};