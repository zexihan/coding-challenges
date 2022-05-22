// Time: O(N^2)
// Space: O(logN)
class Solution {
public:
    int threeSumClosest(vector<int>& nums, int target) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int best = 1e7;

        auto update = [&](int cur) {
            if (abs(cur - target) < abs(best - target)) {
                best = cur;
            }
        };

        for (int i = 0; i < n; ++i) {
            if (i > 0 && nums[i] == nums[i-1])
                continue;
            int j = i + 1, k = n - 1;
            while (j < k) {
                int sum = nums[i] + nums[j] + nums[k];
                if (sum == target)
                    return target;
                update(sum);
                if (sum > target) {
                    --k;
                    while (j < k && nums[k] == nums[k + 1])
                        --k;
                } else {
                    ++j;
                    while (j < k && nums[j] == nums[j-1])
                        ++j;
                }
            }
        }
        return best;
    }
};
