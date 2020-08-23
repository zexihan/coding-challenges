// DP
class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        
        int i, j;
        if (k > n / 2) {
            int sum = 0;
            for (i = 0; i < n - 1; ++i) {
                if (prices[i + 1] > prices[i])
                    sum += prices[i + 1] - prices[i];
            }
            return sum;
        }
        
        vector<vector<int>> f(n + 1, vector<int>(2 * k + 2, 0));
        
        f[0][1] = 0;
        for (i = 2; i <= 2 * k + 1; i++) 
            f[0][i] = INT_MIN;
        
        for (i = 1; i <= n; ++i) {
            for (j = 1; j <= 2 * k + 1; j += 2) {
                f[i][j] = f[i-1][j];
                if (j > 1 && i >= 2 && f[i-1][j-1] != INT_MIN)
                    f[i][j] = max(f[i][j], f[i-1][j-1] + prices[i-1] - prices[i-2]);
            }
            for (j = 2; j <= 2 * k; j += 2) {
                f[i][j] = f[i - 1][j - 1];
                if (i >= 2 && f[i-1][j] != INT_MIN)
                    f[i][j] = max(f[i][j], f[i-1][j] + prices[i-1] - prices[i-2]);
            }
        }
        
        int res = INT_MIN;
        for (i = 1; i <= 2 * k + 1; i += 2)
            res = max(res, f[n][i]);
        
        return res;
    }
};


class Solution {
public:
    int maxProfit(int k, vector<int>& prices) {
        int n = prices.size();
        if (n == 0) return 0;
        
        int i, j;
        if (k > n / 2) {
            int sum = 0;
            for (i = 0; i < n - 1; ++i) {
                if (prices[i + 1] > prices[i])
                    sum += prices[i + 1] - prices[i];
            }
            return sum;
        }
        
        vector<vector<int>> f(2, vector<int>(2 * k + 2, 0));
        int prev = 0, cur = 0;
        
        f[0][1] = 0;
        for (i = 2; i <= 2 * k + 1; i++) 
            f[0][i] = INT_MIN;
        
        for (i = 1; i <= n; ++i) {
            prev = cur;
            cur = 1 - cur;
            for (j = 1; j <= 2 * k + 1; j += 2) {
                f[cur][j] = f[prev][j];
                if (j > 1 && i >= 2 && f[prev][j-1] != INT_MIN)
                    f[cur][j] = max(f[cur][j], f[prev][j-1] + prices[i-1] - prices[i-2]);
            }
            for (j = 2; j <= 2 * k; j += 2) {
                f[cur][j] = f[prev][j - 1];
                if (i >= 2 && f[prev][j] != INT_MIN)
                    f[cur][j] = max(f[cur][j], f[prev][j] + prices[i-1] - prices[i-2]);
            }
        }
        
        int res = INT_MIN;
        for (i = 1; i <= 2 * k + 1; i += 2)
            res = max(res, f[cur][i]);
        
        return res;
    }
};