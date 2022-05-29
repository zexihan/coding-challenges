class Solution {
public:
    int trapRainWater(vector<vector<int>>& heightMap) {
        typedef pair<int, int> cell;
        priority_queue<cell, vector<cell>, greater<cell>> pq;
        int m = heightMap.size();
        if (m == 0) return 0;
        int n = heightMap[0].size();
        vector<bool> visited(m*n, false);
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (i == 0 || i == m-1 || j == 0 || j == n-1) {
                    int idx = i*n+j;
                    if (!visited[idx])
                        pq.push({heightMap[i][j], idx});
                    visited[idx] = true;
                }
            }
        }
        
        vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int res = 0;
        while (!pq.empty()) {
            cell c = pq.top();
            pq.pop();
            int x = c.second / n, y = c.second % n;
            for (auto& d : dirs) {
                int nx = x + d[0];
                int ny = y + d[1];
                int idx = nx*n+ny;
                if (nx < 0 || nx >=m || ny < 0 || ny >= n || visited[idx])
                    continue;
                res += max(0, c.first - heightMap[nx][ny]);
                pq.push({max(c.first, heightMap[nx][ny]), idx});
                visited[idx] = true;
            }
        }
        return res;
    }
};