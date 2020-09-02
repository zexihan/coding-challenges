// DP
// Time: O(mn)
// Space: O(mn)
class Solution {
public:
    int findLength(vector<int>& A, vector<int>& B) {
        int m = A.size(), n = B.size(), res = 0;
        vector<vector<int>> dp(m, vector<int>(n));
        for(int i = 0; i < m; ++i)
            for(int j = 0; j < n; ++j)
                if(A[i] == B[j])
                {
                    dp[i][j] = (i && j ? dp[i - 1][j - 1] : 0) + 1;
                    res = max(res, dp[i][j]);
                }
        return res;
    }
};