// Time: O(n)
// Space: O(1)
class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.size(), left = 0, right = 0;
        while (right < n) {
            if (nums[right]) {
                swap(nums[left], nums[right]);
                left++;
            }
            right++;
        }
    }
};

class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = nums.length;
        int left = 0;
        int right = 0;

        while (right < n) {
            if (nums[right] != 0) {
                nums[right] = nums[left];
                right++;
            }
            left++;
        }

        for (int i = left; i < n; i++){
            nums[i] = 0;
        }
    }
};
