class Solution {
public:
    int m, n;
    int extractSum(int i, int j, const vector<vector<int> >& sum) {
        if (i < 0 || j < 0) return 0;
        if (i >= m) i = m - 1;
        if (j >= n) j = n - 1;
        return sum[i][j];
    }
        
    vector<vector<int>> matrixBlockSum(vector<vector<int>>& mat, int K) {
        m = mat.size();
        n = mat[0].size();
        
        vector<vector<int>> sum(m, vector<int>(n, 0));
        // Calculate prefix matrix 
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                sum[i][j] = mat[i][j] + extractSum(i-1, j, sum) + extractSum(i, j-1, sum) - extractSum(i-1, j-1, sum);
            }
        }
        
        // Use prefix matrix to calculate our sum
        vector<vector<int>> res(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res[i][j] = extractSum(i+K, j+K, sum) - extractSum(i+K, j-K-1,sum) - extractSum (i-K-1, j+K, sum) + extractSum(i-K-1, j-K-1, sum);
            }
        }
        
        return res;
    }
};