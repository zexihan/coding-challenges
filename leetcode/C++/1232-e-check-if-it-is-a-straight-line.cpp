class Solution {
public:
    bool checkStraightLine(vector<vector<int>>& coordinates) {
        int n = coordinates.size();
        int dy = coordinates[1][1] - coordinates[0][1];
        int dx = coordinates[1][0] - coordinates[0][0];
        for (int i = 1; i < n - 1; i++) {
            int dy_new = coordinates[i+1][1] - coordinates[i][1];
            int dx_new = coordinates[i+1][0] - coordinates[i][0];
            if (dy * dx_new != dx * dy_new) return false;
        }
        return true;
    }
};