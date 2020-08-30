class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        vector<int> steps = {n , n-1};
        vector<vector<int>> matrix(n, vector<int>(n));
        int dIdx = 0, sIdx = 0;
        int r = 0, c = -1;
        int num = 1;
        while (steps[sIdx] > 0) {
            for (int i = 0; i < steps[sIdx]; i++) {
                r += directions[dIdx][0], c += directions[dIdx][1];
                matrix[r][c] = num;
                num++;
            }
            steps[sIdx]--;
            dIdx = (dIdx + 1) % 4;
            sIdx = (sIdx + 1) % 2;
        }
        return matrix;
    }
};