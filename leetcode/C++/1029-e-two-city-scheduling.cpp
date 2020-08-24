// Greedy
class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        auto compare = [](vector<int>& a, vector<int>& b){
            return a[0] - a[1] < b[0] - b[1];
        };
        sort(costs.begin(), costs.end(), compare);
        int n = costs.size() / 2;
        int res = 0;
        for (int i = 0; i < n; i++)
            res += costs[i][0] + costs[i + n][1];
        return res;
    }
};