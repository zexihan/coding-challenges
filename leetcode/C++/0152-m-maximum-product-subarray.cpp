// DP
// Time: O(n)
// Space: O(n)
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int n = nums.size();
        int res = INT_MIN;
        if (n == 0)
            return 0;
        
        vector<int> f(n, 0);
        vector<int> g(n, 0);
        for (int i = 0; i < n; i++) {
            f[i] = nums[i];
            if (i > 0) 
                f[i] = max(f[i], max(nums[i] * f[i-1], nums[i] * g[i-1]));
            
            g[i] = nums[i];
            if (i > 0) 
                g[i] = min(g[i], min(nums[i] * f[i-1], nums[i] * g[i-1]));
            
            res = max(res, f[i]);
        }
        return res;
    }
};