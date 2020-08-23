// DP
class Solution {
public:
    int helper(vector<int>& nums) {
        int prevMax = 0;
        int curMax = 0;
        for (int x : nums) {
            int tmp = curMax;
            curMax = max(prevMax + x, curMax);
            prevMax = tmp;
        }
        return curMax;
    }
    
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
};