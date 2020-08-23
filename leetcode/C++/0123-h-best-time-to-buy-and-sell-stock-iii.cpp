// DP
// phase 1, 3, 5:
// f[i][j] = max(f[i - 1][j], f[i-1][j-1] + prices[i-1] - prices[i-2])
// phase 2, 4:
// f[i][j] = max(f[i-1][j-1], f[i-1][j] + prices[i-1] - prices[i-2])
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        
        vector<vector<int>> f(n + 1, vector<int>(5 + 1, 0));
        int i, j;
        f[0][1] = 0;
        for (i = 2; i <= 5; i++) 
            f[0][i] = INT_MIN;
        
        for (i = 1; i <= n; ++i) {
            for (j = 1; j<=5; j += 2) {
                f[i][j] = f[i-1][j];
                if (j > 1 && i >= 2 && f[i-1][j-1] != INT_MIN)
                    f[i][j] = max(f[i][j], f[i-1][j-1] + prices[i-1] - prices[i-2]);
            }
            for (j = 2; j<=4; j += 2) {
                f[i][j] = f[i - 1][j - 1];
                if (i >= 2 && f[i-1][j] != INT_MIN)
                    f[i][j] = max(f[i][j], f[i-1][j] + prices[i-1] - prices[i-2]);
            }
        }
        return max(f[n][1], max(f[n][3], f[n][5]));
    }
};