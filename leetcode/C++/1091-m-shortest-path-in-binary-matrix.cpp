class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        int N = grid.size();
        if (grid[0][0] != 0 || grid[N-1][N-1] == 1) return -1;
        queue<pair<int, int>> q;
        q.push({0, 0});
        int len = 0;
        grid[0][0] = 2;
        vector<pair<int, int>> dirs = {{0,1}, {1,0}, {0,-1}, {-1,0}, {1,1}, {1,-1}, {-1,1}, {-1,-1}};
        while (!q.empty()) {
            int size = q.size();
            len++;
            for (int s = 0; s < size; s++) {
                auto curr = q.front(); q.pop();
                int x = curr.first, y = curr.second;
                if (x == N-1 && y == N-1) return len;
                for (auto& dir: dirs) {
                    int nx = x + dir.first, ny = y + dir.second;
                    if (0 <= nx && nx < N && 0 <= ny && ny < N && grid[nx][ny] == 0) 
                        q.push({nx, ny}), grid[nx][ny] = 2;
                }
            }
        }
        return -1;
    }
};