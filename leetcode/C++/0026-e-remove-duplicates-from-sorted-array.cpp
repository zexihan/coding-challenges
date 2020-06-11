class Solution {
public:
    int removeDuplicates(vector<int>& nums) {
        if (nums.empty())
            return 0;
        int index = 0;
        for (int i = 1; i < nums.size(); i++) {
            if (nums[index] != nums[i])
                nums[++index] = nums[i];
        }
        return index + 1;
    }
};

class Solution {
public:
    int removeDuplicates(vector<int> &nums) {
        return distance(nums.begin(), unique(nums.begin(), nums.end()));
    }
};