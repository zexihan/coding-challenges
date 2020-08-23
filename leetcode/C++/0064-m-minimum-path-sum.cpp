// DP
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<int>> f(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    f[i][j] = grid[i][j];
                    continue;
                }
                
                int t = INT_MAX;
                if (i > 0)
                    t = min(t, f[i-1][j]);
                if (j > 0)
                    t = min(t, f[i][j-1]);
                
                f[i][j] = t + grid[i][j];
            }
        }
        return f[m-1][n-1];
    }
};

// Space optimized DP
class Solution {
public:
    int minPathSum(vector<vector<int>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;
        
        vector<vector<int>> f(2, vector<int>(n, 0));
        int prev = 0, cur = 0;
        for (int i = 0; i < m; i++) {
            prev = cur;
            cur = 1 - cur;
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) {
                    f[cur][j] = grid[i][j];
                    continue;
                }
                
                int t = INT_MAX;
                if (i > 0)
                    t = min(t, f[prev][j]);
                if (j > 0)
                    t = min(t, f[cur][j-1]);
                
                f[cur][j] = t + grid[i][j];
            }
        }
        return f[cur][n-1];
    }
};