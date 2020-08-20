// Binary search
// Time: O(logN)
// Space: O(1)
class Solution {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 0) return -1;
        int l = 0, r = nums.size() - 1;
        while (l < r - 1) {
            if (nums[l] < nums[r])
                return nums[l];
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[l])
                l = mid;
            else
                r = mid;
        }
        return min(nums[l], nums[r]);
    }
};