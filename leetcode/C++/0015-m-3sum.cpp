// Two pointers
// Time: O(N^2)
// Space: O(1)
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        if (nums.size() < 3) return res;
        sort(nums.begin(), nums.end());
        for (auto i = nums.begin(); i < nums.end() - 2; i++) {
            auto j = i + 1, k = nums.end() - 1;
            if (i > nums.begin() && *i == *(i - 1))
                continue;
            while (j < k) {
                if (*i + *j + *k < 0) {
                    j++;
                    while (*j == *(j - 1) && j < k)
                        j++;
                } else if (*i + *j + *k > 0) {
                    k--;
                    while (*k == *(k + 1) && j < k)
                        k--;
                } else {
                    res.push_back({*i, *j, *k});
                    j++;
                    k--;
                    while (*j == *(j - 1) && *k == *(k + 1) && j < k)
                        j++;
                }
            }
        }
        return res;
    }
};

// HashSet + TwoSum
class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        vector<vector<int>> res;
        for (int i = 0; i < nums.size() && nums[i] <= 0; ++i) {
            if (i == 0 || nums[i-1] != nums[i])
                twoSum(nums, i, res);
        }
        return res;
    }
    
    void twoSum(vector<int>& nums, int i, vector<vector<int>>& res) {
        unordered_set<int> seen;
        for (int j = i + 1; j < nums.size(); j++) {
            int complement = -nums[i] - nums[j];
            if (seen.find(complement) != seen.end()) {
                res.push_back({nums[i], nums[j], complement});
                while (j < nums.size() - 1 && nums[j] == nums[j + 1])
                    j++;
            }
            seen.insert(nums[j]);
        }
    }
};