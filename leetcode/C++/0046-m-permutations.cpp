// DFS
// Time: O(n! * n)
// Space: O(n!)
class Solution {
public:
    void helper(vector<int>& nums, vector<int>& path, vector<vector<int>>& res) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int n : nums) {
            vector<int>::iterator it = find(path.begin(), path.end(), n);
            if (it != path.end())
                continue;
            path.push_back(n);
            helper(nums, path, res);
            path.pop_back();
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0)
            return res;
        vector<int> path;
        helper(nums, path, res);
        return res;
    }
};

// DFS + Swap
class Solution {
public: 
    void helper(vector<int>& nums, int pos, vector<vector<int>>& res) {
        if (pos == nums.size()) {
            res.push_back(nums);
            return;
        }
        for (int i = pos; i < nums.size(); i++) {
            swap(nums[i], nums[pos]);
            helper(nums, pos + 1, res);
            swap(nums[i], nums[pos]);
        }
    }
    
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0)
            return res;
        helper(nums, 0, res);
        return res;
    }
};