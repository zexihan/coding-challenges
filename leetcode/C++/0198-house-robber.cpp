// DP
// f(k) = max(f(k – 2) + Ak, f(k – 1))
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int rob(vector<int>& nums) {
        int prevMax = 0;
        int curMax = 0;
        for (int x : nums) {
            int tmp = curMax;
            curMax = max(prevMax + x, curMax);
            prevMax = tmp;
        }
        return curMax;
    }
};