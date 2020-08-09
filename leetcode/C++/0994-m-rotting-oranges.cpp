// BFS
// Time: O(mn)
// Space: O(mn)
class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        queue<pair<int, int>> q;
        
        // build the initial set of rotten oranges
        int freshOranges = 0;
        int ROWS = grid.size();
        int COLS = grid[0].size();
        
        for (int r = 0; r < ROWS; ++r)
            for (int c = 0; c < COLS; ++c)
                if (grid[r][c] == 2)
                    q.push({r, c});
                else if (grid[r][c] == 1)
                    freshOranges++;
        
        // Mark the round / level, i.e. the ticker of timestamp
        q.push({-1, -1});
        
        // start the rotting process via BFS
        int minutesElapsed = -1;
        vector<pair<int, int>> directions = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};
        
        while (!q.empty()) {
            pair<int, int> p = q.front();
            q.pop();
            int row = p.first;
            int col = p.second;
            if (row == -1) {
                minutesElapsed++;
                if (!q.empty())
                    q.push({-1, -1});
            } else {
                for (pair<int, int> d : directions) {
                    int neighborRow = row + d.first;
                    int neighborCol = col + d.second;
                    if (neighborRow >= 0 && neighborRow < ROWS &&
                        neighborCol >= 0 && neighborCol < COLS) {
                        if (grid[neighborRow][neighborCol] == 1) {
                            grid[neighborRow][neighborCol] = 2;
                            freshOranges--;
                            q.push({neighborRow, neighborCol});
                        }
                    }
                }
            }
        }
        
        return freshOranges == 0 ? minutesElapsed : -1;
    }
};