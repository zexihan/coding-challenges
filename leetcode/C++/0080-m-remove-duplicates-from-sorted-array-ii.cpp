// Time: O(n)
// Space: O(1)
class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        int n = nums.size();
        int cur = 0;
        for (int i = 0; i < n; ++i) {
            nums[cur++] = nums[i];
            if (cur >= 3 && nums[cur-1] == nums[cur-2] && nums[cur-2] == nums[cur-3])
                cur--;
        }
        return cur;
    }
};