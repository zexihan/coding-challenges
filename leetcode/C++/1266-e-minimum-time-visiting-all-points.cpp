class Solution {
public:
    int minTimeToVisitAllPoints(vector<vector<int>>& points) {
        int res = 0;
        int dx, dy;
        for (int i = 0; i < points.size() - 1; i++) {
            dx = abs(points[i+1][0] - points[i][0]);
            dy = abs(points[i+1][1] - points[i][1]);
            res += max(dx, dy);
        }
        return res;
    }
};