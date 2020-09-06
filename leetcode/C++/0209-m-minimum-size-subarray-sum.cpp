// Prefix sum
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        int sum = 0, res = INT_MAX;
        int i = 0, j = 0;
        for (; i < n; i++) {
            while (j < n && sum < s) {
                sum += nums[j];
                j++;
            }
            if (sum >= s) 
                res = min(res, j - i);
            sum -= nums[i];
        }
        if (res == INT_MAX) return 0;
        return res;
    }
};