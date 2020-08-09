// backtrack
class Solution {
public:
    void helper(vector<int>& nums, int pos, vector<int>& path, vector<vector<int>>& res) {
        res.push_back(path);
        for (int i = pos; i < nums.size(); i++) {
            if (i != pos && nums[i] == nums[i-1])
                continue;
            path.push_back(nums[i]);
            helper(nums, i + 1, path, res);
            path.pop_back();
        }
    }
    
    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0)
            return res;
        vector<int> path;
        sort(nums.begin(), nums.end());
        helper(nums, 0, path, res);
        return res;
    }
};