// DP
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        if (matrix.empty() || matrix[0].empty())
            return 0;
        int n_row = matrix.size(), n_col = matrix[0].size();
        vector<vector<int>> dp(n_row, vector<int>(n_col, 0));
        
        int res = 0;
        for (int r = 0; r < n_row; r++) {
            for (int c = 0; c < n_col; c++) {
                dp[r][c] = matrix[r][c] - '0';
                if (r > 0 && c > 0 && dp[r][c] == 1) {
                    dp[r][c] += min(min(dp[r-1][c-1], dp[r][c-1]), dp[r-1][c]);
                }
                res = max(res, dp[r][c]);
            }
        }
        return res * res;
    }
};