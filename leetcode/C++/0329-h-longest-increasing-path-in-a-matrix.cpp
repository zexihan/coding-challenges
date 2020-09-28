class Solution {
private:
    int m;
    int n;
    vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    int dfs(vector<vector<int>>& matrix, vector<vector<int>>& cache, 
             int i, int j) {
        if (cache[i][j] != 0) return cache[i][j];
        cache[i][j] = 1;
        for (auto& d : dirs) {
            int x = i + d[0], y = j + d[1];
            if (x < 0 || y < 0 || x >= m || y >= n || matrix[x][y] <= matrix[i][j])
                continue;
            cache[i][j] = max(cache[i][j], dfs(matrix, cache, x, y) + 1);
        }
        return cache[i][j];
    }
    
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if (m == 0) return 0;
        n = matrix[0].size();
        int res = 0;
        vector<vector<int>> cache(m, vector<int>(n, 0));
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                res = max(res, dfs(matrix, cache, i, j));
            }
        }
        return res;
    }
};