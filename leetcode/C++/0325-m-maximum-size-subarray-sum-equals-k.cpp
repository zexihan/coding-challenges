class Solution {
public:
    int maxSubArrayLen(vector<int>& nums, int k) {
        int n = nums.size();
        unordered_map<int, int> mp{{0, -1}};
        int sum = 0, res = INT_MIN;
        for (int i = 0; i < n; i++) {
            sum += nums[i];
            if (mp.find(sum - k) != mp.end())
                res = max(res, i - mp[sum - k]);
            if (mp.find(sum) == mp.end())
                mp[sum] = i;
        }
        if (res == INT_MIN) return 0;
        return res;
    }
};