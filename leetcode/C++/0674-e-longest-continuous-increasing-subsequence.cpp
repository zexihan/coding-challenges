// DP
class Solution {
public:
    int findLengthOfLCIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> f(n, 1);
        int res = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1])
                f[i] = max(1, f[i-1] + 1);
            res = max(res, f[i]);
        }
        return res;
    }
};