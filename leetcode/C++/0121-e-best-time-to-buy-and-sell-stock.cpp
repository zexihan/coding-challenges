// Prefix min
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        int res = 0;
        int prefix_min = prices[0];
        for (int i = 1; i < n; ++i) {
            res = max(res, prices[i] - prefix_min);
            prefix_min = min(prefix_min, prices[i]);
        }
        return res;
    }
};