// DP
class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        
        vector<vector<int>> f(n + 1, vector<int>(3, INT_MAX));
        f[0][0] = 0, f[0][1] = 0, f[0][2] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 0; j < 3; j++) {
                for (int k = 0; k < 3; k++) {
                    if (j != k)
                        f[i][j] = min(f[i][j], f[i-1][k] + costs[i-1][j]);
                }
            }
        }
        return min(f[n][0], min(f[n][1], f[n][2]));
    }
};