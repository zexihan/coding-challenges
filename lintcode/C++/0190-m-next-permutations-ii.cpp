//    1,2,7,4,3,1
// -> 1,3,1,2,4,7
class Solution {
    public:
        void nextPermutation(vector<int> &nums) {
            int n = nums.size(), i = n - 2, j = n - 1;
            while (i >= 0 && nums[i] >= nums[i + 1]) 
                --i;
            if (i >= 0) {
                while (nums[j] <= nums[i])
                    --j;
                swap(nums[i], nums[j]);
            }
            reverse(nums.begin() + i + 1, nums.end());
        }
};