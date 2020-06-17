class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        if (matrix.empty() || matrix[0].empty())
            return vector<int>();
        int m = matrix.size(), n = matrix[0].size();
        vector<int> res(m * n, 0);

        vector<vector<bool>> trace(m, vector<bool>(n, false));
        int x = 0, y = 0;
        // direction: o-right, 1-down, 2-left, 3-up
        int direction = 0;
        int i = 1;
        res[0] = matrix[x][y];
        trace[0][0] = true;

        while (i < m * n) {
            int tmp_x = x, tmp_y = y;
            switch(direction) {
                case 0:
                    y += 1;
                    break;
                case 1:
                    x += 1;
                    break;
                case 2:
                    y -= 1;
                    break;
                case 3:
                    x -= 1;
                    break;
            }

            if (x < 0 || y < 0 || x >= m || y >= n || trace[x][y]) {
                direction = (direction + 1) % 4;
                x = tmp_x, y = tmp_y;
                continue;
            }

            res[i] = matrix[x][y];
            trace[x][y] = true;
            i++;
        }
        return res;
    }
};