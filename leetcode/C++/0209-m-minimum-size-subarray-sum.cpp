// Two pointers
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int n = nums.size();
        int j = 0;
        int curSum = 0;
        int res = INT_MAX;
        for (int i = 0; i < n; i++) {
            while (j < n && curSum < s) {
                curSum += nums[j];
                j++;
            }
            
            if (curSum >= s) 
                res = min(res, j - i);
            
            curSum -= nums[i];
        }
        return res != INT_MAX ? res : 0;
    }
};