class Solution {
    public:
        int maxSubArray(vector<int> nums) {
            int sum = 0, minSum = 0, maxSum = INT_MIN;
            for (int i = 0; i < nums.size(); i++) {
                sum += nums[i];
                maxSum = max(maxSum, sum - minSum);
                minSum = min(minSum, sum);
            }
            return maxSum;
        }
};