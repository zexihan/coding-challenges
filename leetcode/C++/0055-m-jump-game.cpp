// Greedy
// Time: O(n)
// Space: O(1)
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        int next_pos = 0;
        for (int i = 0; i < n; i++) {
            if (i <= next_pos && i + nums[i] >= next_pos)
                next_pos = i + nums[i];
        }
        return next_pos >= n - 1;
    }
};


// DP
// Time: O(n^2)
// Space: O(n)
class Solution {
public:
    bool canJump(vector<int>& nums) {
        int n = nums.size();
        vector<bool> f(n, false);
        
        f[0] = true;
        for (int j = 1; j < n; j++) {
            for (int i = 0; i < j; i++) {
                if (f[i] && i + nums[i] >= j) {
                    f[j] = true;
                    break;
                }
            }
        }
        
        return f[n - 1];
    }
};