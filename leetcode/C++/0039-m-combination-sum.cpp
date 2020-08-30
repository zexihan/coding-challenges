class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> path;
        dfs(candidates, target, 0, path, res);
        return res;
    }
    
    void dfs(vector<int>& candidates, int target, int start, 
             vector<int>& path, vector<vector<int>>& res) {
        if (target == 0)
            res.push_back(path);
        for (int i = start; i < candidates.size(); i++) {
            if (candidates[i] > target)
                return;
            path.push_back(candidates[i]);
            dfs(candidates, target - candidates[i], i, path, res);
            path.pop_back();
        }
    }
};