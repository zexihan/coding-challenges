// Prefix sum
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        if (nums.empty()) return 0;
        unordered_map<int, int> counts{{0, 1}};
        int res = 0, sum = 0;
        for (int num : nums) {
            sum += num;
            // cur_prefix_sum - some_prefix_sum = k
            if (counts.find(sum - k) != counts.end())
                res += counts[sum - k];
            counts[sum]++;
        }
        return res;
    }
};