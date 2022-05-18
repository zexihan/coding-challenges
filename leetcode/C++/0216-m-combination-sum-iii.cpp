class Solution {
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        vector<vector<int>> res;
        dfs(1, 9, k, n, path, res);
        return ans;
    }

    void dfs(int cur, int n, int k, int sum, vector<int>& path, vector<vector<int>>& res) {
        if (path.size() + (n - cur + 1) < k || path.size() > k) {
            return;
        }
        if (path.size() == k && accumulate(path.begin(), path.end(), 0) == sum) {
            res.push_back(path);
            return;
        }
        path.push_back(cur);
        dfs(cur + 1, n, k, sum, path, res);
        path.pop_back();
        dfs(cur + 1, n, k, sum, path, res);
    }
};
