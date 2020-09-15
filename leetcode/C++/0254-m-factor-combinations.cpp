class Solution {
private:
    void helper(int start, int n, vector<int>& path, vector<vector<int>>& res) {
        for (int i = start; i <= sqrt(n); i++) {
            if (n % i == 0) {
                path.push_back(i);
                helper(i, n / i, path, res);
                path.push_back(n / i);
                res.push_back(path);
                path.pop_back();
                path.pop_back();
            }
        }
    }
    
public:
    vector<vector<int>> getFactors(int n) {
        vector<int> path;
        vector<vector<int>> res;
        if (n == 1) return res;
        helper(2, n, path, res);
        return res;
    }
};