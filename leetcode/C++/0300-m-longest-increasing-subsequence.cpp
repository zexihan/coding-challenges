// DP
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> f(n, 1);
        int res = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i; ++j) {
                if (nums[j] < nums[i])
                    f[i] = max(f[i], f[j] + 1);
            }
            res = max(res, f[i]);
        }
        return res;
    }
};