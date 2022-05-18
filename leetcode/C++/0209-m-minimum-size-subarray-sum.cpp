// Prefix sum
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int n = nums.size();
        int sum = 0, res = INT_MAX;
        for (int i = 0, j = 0; i < n; i++) {
            while (j < n && sum < target) {
                sum += nums[j];
                j++;
            }
            if (sum >= target) 
                res = min(res, j - i);
            sum -= nums[i];
        }
        if (res == INT_MAX) return 0;
        return res;
    }
};