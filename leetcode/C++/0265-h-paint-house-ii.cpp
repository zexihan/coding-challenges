// DP
class Solution {
public:
    int minCostII(vector<vector<int>>& costs) {
        int n = costs.size();
        if (n == 0) return 0;
        
        int K = costs[0].size();
        if (n == 1 && K == 1) return costs[0][0];
        if (K == 1) return INT_MAX;
        vector<vector<int>> f(n + 1, vector<int>(K, 0));
        int i, j;
        int min1, min2;
        int id1 = 0, id2 = 0;
        for (i = 1; i <= n ; ++i) {
            min1 = INT_MAX, min2 = INT_MAX;
            for (j = 0; j < K; ++j) {
                if (f[i-1][j] < min1) {
                    min2 = min1;
                    id2 = id1;
                    min1 = f[i-1][j];
                    id1 = j;
                } else {
                    if (f[i-1][j] < min2) {
                        min2 = f[i-1][j];
                        id2 = j;
                    }
                }
            }
            for (j = 0; j < K; ++j) {
                f[i][j] = costs[i-1][j];
                if (j != id1)
                    f[i][j] += min1;
                else
                    f[i][j] += min2;
            } 
        }
        int res = INT_MAX;
        for (i = 0; i < K; ++i) 
            res = min(res, f[n][i]);
        return res;
    }
};