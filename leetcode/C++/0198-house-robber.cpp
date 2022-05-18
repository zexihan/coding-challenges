// DP
// f(k) = max(f(k – 2) + Ak, f(k – 1))
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int rob(vector<int>& nums) {
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