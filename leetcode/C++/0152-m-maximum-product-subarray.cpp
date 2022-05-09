// DP
// fmax[i] = max(fmax[i-1] * a[i], fmin[i-1] * a[i], a[i])
// fmin[i] = min(fmax[i-1] * a[i], fmin[i-1] * a[i], a[i])

// Time: O(n)
// Space: O(n)
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        vector <int> maxF(nums), minF(nums);
        for (int i = 1; i < nums.size(); ++i) {
            maxF[i] = max(maxF[i - 1] * nums[i], max(nums[i], minF[i - 1] * nums[i]));
            minF[i] = min(minF[i - 1] * nums[i], min(nums[i], maxF[i - 1] * nums[i]));
        }
        return *max_element(maxF.begin(), maxF.end());
    }
};

// Time: O(n)
// Space: O(1)
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxF = nums[0], minF = nums[0], res = nums[0];
        for (int i = 1; i < nums.size(); ++i) {
            int mx = maxF, mn = minF;
            maxF = max(mx * nums[i], max(nums[i], mn * nums[i]));
            minF = min(mn * nums[i], min(nums[i], mx * nums[i]));
            res = max(maxF, res);
        }
        return res;
    }
};
