// DP
class Solution {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if (n == 0) return 0;
        if (n == 1) return nums[0];
        
        vector<int> A(n-1, 0);
        int res = INT_MIN;
        for (int i = 0; i < n - 1; ++i)
            A[i] = nums[i];
        res = max(res, helper(A));
        
        for (int i = 0; i < n - 1; ++i) 
            A[i] = nums[i + 1];
        res = max(res, helper(A));
        
        return res;
    }

    int helper(vector<int>& nums) {
        int prev_max = 0;
        int curr_max = 0;
        for (int x : nums) {
            int tmp = curr_max;
            curr_max = max(prev_max + x, curr_max);
            prev_max = tmp;
        }
        return curr_max;
    }
};