class Solution {
public:
    int jump(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) return 0;
        
        int max_pos = nums[0];
        int max_steps = nums[0];
        int jumps = 1;
        for (int i = 1; i < n; i++) {
            if (max_steps < i) {
                jumps++;
                max_steps = max_pos;
            }
            max_pos = max(max_pos, nums[i] + i);
        }
        return jumps;
    }
};