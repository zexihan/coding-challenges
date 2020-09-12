// dp[i, j] = dp[i, k] + dp[k + 1, j] + max(A[i, k]) * max(A[k + 1, j])
class Solution {
public:
    int mctFromLeafValues(vector<int>& arr) {
        int n = arr.size();
        vector<vector<int>> dp(n, vector<int>(n, INT_MAX));
        for (int i = 0; i < n; i++)
            dp[i][i] = 0;
        
        int l, i, j, k;
        int rootVal;
        auto beg = arr.begin();
        for (l = 2; l < n + 1; l++) {
            for (i = 0; i < n - l + 1; i++) {
                j = i + l - 1;
                for (k = i; k < j; k++) {
                    rootVal = *max_element(beg + i, beg + k + 1) * *max_element(beg + k + 1, beg + j + 1);
                    dp[i][j] = min(dp[i][j], rootVal + dp[i][k] + dp[k+1][j]);
                }
            }
        }
        return dp[0][n-1];
    }
};
