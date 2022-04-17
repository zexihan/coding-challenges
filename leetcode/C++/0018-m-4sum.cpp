class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        sort(begin(nums), end(nums));
        return kSum(nums, target, 0, 4);
    }
    
    vector<vector<int>> kSum(vector<int>& nums, int target, int start, int k) {
        vector<vector<int>> res;
        if (start == nums.size() || nums[start] * k > target || target > nums.back() * k)
            return res;
        if (k == 2)
            return twoSum(nums, target, start);
        for (int i = start; i < nums.size(); ++i)
            if (i == start || nums[i - 1] != nums[i])
                for (auto &set : kSum(nums, target - nums[i], i + 1, k - 1)) {
                    res.push_back({nums[i]});
                    res.back().insert(end(res.back()), begin(set), end(set));
                }
        return res;
    }
    
    vector<vector<int>> twoSum(vector<int>& nums, int target, int start) {
        vector<vector<int>> res;
        int lo = start, hi = nums.size() - 1;
        while (lo < hi) {
            int sum = nums[lo] + nums[hi];
            if (sum < target || (lo > start && nums[lo] == nums[lo - 1]))
                ++lo;
            else if (sum > target || (hi < nums.size() - 1 && nums[hi] == nums[hi + 1]))
                --hi;
            else
                res.push_back({ nums[lo++], nums[hi--]});
        }
        return res;
    }
};


class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int>> res;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 3; i++) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            if ((long) nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target)
                break;
            if ((long) nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target)
                continue;
            for (int j = i+1; j < n - 2; j++) {
                if (j > i+1 && nums[j] == nums[j-1])
                    continue;
                if ((long) nums[i] + nums[j] + nums[j+1] + nums[j+2] > target)
                    break;
                if ((long) nums[i] + nums[j] + nums[n-2] + nums[n-1] < target)
                    continue;
                int left = j + 1;
                int right = n - 1;
                while (left < right) {
                    if (nums[left] + nums[right] < target - nums[i] - nums[j])
                        left++;
                    else if (nums[left] + nums[right] > target - nums[i] - nums[j])
                        right--;
                    else {
                        res.push_back({nums[i], nums[j], nums[left++], nums[right--]});
                        while (left < right && nums[left] == nums[left-1])
                            left++;
                        while (left < right && nums[right] == nums[right+1])
                            right--;
                    }
                }
            }
        }
        return res;
    }
};