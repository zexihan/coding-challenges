class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        vector<int> res;
        int m = matrix.size();
        if (m == 0) return res;
        int n = matrix[0].size();
        vector<vector<int>> dirs = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<int> steps = {n, m - 1};
        int dIdx = 0, sIdx = 0;
        int i = 0, j = -1;
        while (steps[0] > -1 && steps[1] > -1) {
            for (int k = 0; k < steps[sIdx]; k++) {
                i += dirs[dIdx][0];
                j += dirs[dIdx][1];
                res.push_back(matrix[i][j]);
            }
            steps[sIdx]--;
            sIdx = (sIdx + 1) % 2;
            dIdx = (dIdx + 1) % 4;
        }
        return res;
    }
};