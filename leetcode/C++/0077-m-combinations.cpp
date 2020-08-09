// backtrack
class Solution {
public:
    void helper(int n, int k, int pos, vector<int>& path, vector<vector<int>>& res) {
        if (path.size() == k) {
            res.push_back(path);
            return;
        }
        for (int i = pos; i <= n; i++) {
            path.push_back(i);
            helper(n, k, i + 1, path, res);
            path.pop_back();
        }
    }
    
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        if (n < 1 || k == 0)
            return res;
        vector<int> path;
        helper(n, k, 1, path, res);
        return res;
    }
};