class Solution {
public:
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        auto compare = [](vector<int> a, vector<int> b){
            int dista = a[0] * a[0] + a[1] * a[1];
            int distb = b[0] * b[0] + b[1] * b[1];
            return dista < distb;
        };
        partial_sort(points.begin(), points.begin() + K, points.end(), compare);
        return vector<vector<int>>(points.begin(), points.begin() + K);
    }
};
