class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0, minSum = 0, res = INT_MIN;
        for (size_t i = 0; i < nums.size(); i++) {
            sum += nums[i];
            res = max(res, sum - minSum);
            minSum = min(minSum, sum);
        }
        return res;
    }
};