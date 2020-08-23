// DP
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        vector<int> f(n, 1);
        int i, j;
        int res = 0;
        for (int j = 0; j < n; j++) {
            for (i = 0; i < j; ++i) {
                if (nums[i] < nums[j])
                    f[j] = max(f[j], f[i] + 1);
            }
            res = max(res, f[j]);
        }
        return res;
    }
};