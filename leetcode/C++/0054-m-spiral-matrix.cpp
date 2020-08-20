class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<vector<int> > dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<int> res;
        int nr = matrix.size();     if (nr == 0) return res;
        int nc = matrix[0].size();  if (nc == 0) return res;

        vector<int> nSteps{nc, nr-1};

        int iDir = 0;   // index of direction.
        int ir = 0, ic = -1;    // initial position
        while (nSteps[iDir%2]) {
            for (int i = 0; i < nSteps[iDir%2]; ++i) {
                ir += dirs[iDir][0]; ic += dirs[iDir][1];
                res.push_back(matrix[ir][ic]);
            }
            nSteps[iDir%2]--;
            iDir = (iDir + 1) % 4;
        }
        return res;
    }
};


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