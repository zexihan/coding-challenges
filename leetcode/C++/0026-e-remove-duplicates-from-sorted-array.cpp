class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty())
            return 0;
        int cur = 0;
        for (int i = 0; i < nums.size(); i++) {
            nums[cur++] = nums[i];
            if (cur >= 2 && nums[cur-1] == nums[cur-2])
                cur--;
        }
        return cur;
    }
};

class Solution {
public:
    int removeDuplicates(vector<int> &nums) {
        return distance(nums.begin(), unique(nums.begin(), nums.end()));
    }
};