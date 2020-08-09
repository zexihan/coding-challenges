class Solution {
public:
       
    void helper(vector<int>& nums, vector<int>& path, vector<bool>& visited, vector<vector<int>>& res) {
        if (path.size() == nums.size()) {
            res.push_back(path);
            return;
        }
        for (int i = 0; i < nums.size(); i++) {
            if (visited[i] || 
                (i != 0 && nums[i] == nums[i-1] && !visited[i-1]))
                continue;
            visited[i] = true;
            path.push_back(nums[i]);
            helper(nums, path, visited, res);
            path.pop_back();
            visited[i] = false;
        }
    }
    
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0)
            return res;
        vector<int> path;
        vector<bool> visited(nums.size(), false);
        sort(nums.begin(), nums.end());
        helper(nums, path, visited, res);
        return res;
    }
};


// DFS + Swap
class Solution {
public:
    void swap(vector<int>& nums, int i, int j) {
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
    
    void helper(vector<int>& nums, int pos, vector<vector<int>>& res) {
        if (pos == nums.size()) {
            res.push_back(nums);
            return;
        }
        unordered_set<int> used;
        for (int i = pos; i < nums.size(); i++) {
            if (used.find(nums[i]) == used.end()) {
                used.insert(nums[i]);
                swap(nums, i, pos);
                helper(nums, pos + 1, res);
                swap(nums, i, pos);
            }
        }
    }
    
    
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() == 0)
            return res;
        helper(nums, 0, res);
        return res;
    }
};