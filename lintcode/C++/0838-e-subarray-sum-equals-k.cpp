// Time: O(n^2)
// Space: O(n)
class Solution_1 {
public:
    int subarraySumEqualsK (vector<int> &nums, int k) {
        const int n = nums.size();
        vector<int> sums(n + 1, 0);
        for (int i = 1; i <= n; ++i)
            sums[i] = sums[i - 1] + nums[i - 1];
        int ans = 0;
        for (int i = 0; i < n; ++i)
            for (int j = i; j < n; ++j)
                if (sums[j + 1] - sums[i] == k)
                    ++ans;
        return ans;
    }
};

// Let sum = nums[0] + ... + nums[i]
// Check how many prefix sums (j's, j < i) equal to sum - k
// nums[0] + ... + nums[j] = sum - k
// then there are the same number of j's that nums[j + 1] + ... + nums[i] = k
// Time: O(n)
// Space: O(n)
class Solution_2 {
public:
    int subarraySumEqualsK (vector<int> &nums, int k) {
        if (nums.empty()) return 0;
        unordered_map<int, int> counts{{0, 1}};
        int ans = 0;
        int sum = 0;
        for (const int num : nums) {
            sum += num;
            ans += counts[sum - k];
            ++counts[sum];
        }
        return ans;
    }
};