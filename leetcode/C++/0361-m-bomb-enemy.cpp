// DP
class Solution {
public:
    int maxKilledEnemies(vector<vector<char>>& grid) {
        int m = grid.size();
        if (m == 0) return 0;
        int n = grid[0].size();
        if (n == 0) return 0;

        vector<vector<int>> up(m, vector<int>(n, 0));
        vector<vector<int>> down(m, vector<int>(n, 0));
        vector<vector<int>> left(m, vector<int>(n, 0));
        vector<vector<int>> right(m, vector<int>(n, 0));

        int res = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 'W') {
                    up[i][j] = 0;
                    continue;
                }
                up[i][j] = grid[i][j] == 'E' ? 1 : 0;
                if (i > 0)
                    up[i][j] += up[i-1][j];
            }
        }
                
        for (int i = m - 1; i > -1; i--) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 'W') {
                    down[i][j] = 0;
                    continue;
                }
                    
                down[i][j] = grid[i][j] == 'E' ? 1 : 0;
                if (i < m - 1)
                    down[i][j] += down[i+1][j];
            }
        }  

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 'W') {
                    left[i][j] = 0;
                    continue;
                }  
                left[i][j] = grid[i][j] == 'E' ? 1 : 0;
                if (j > 0)
                    left[i][j] += left[i][j-1];
            }  
        }

        for (int i = 0; i < m; i++) {
            for (int j = n - 1; j > -1; j--) {
                if (grid[i][j] == 'W') {
                    right[i][j] = 0;
                    continue;
                }
                right[i][j] = grid[i][j] == 'E' ? 1 : 0;
                if (j < n - 1)
                    right[i][j] += right[i][j+1];
            }  
        }
            

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '0') {
                    int t = up[i][j] + left[i][j] + down[i][j] + right[i][j];
                    res = max(t, res);
                }
            }
        }
        return res;       
    }
};