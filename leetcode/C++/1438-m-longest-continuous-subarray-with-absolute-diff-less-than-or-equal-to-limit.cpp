// multiset
class Solution {
public:
    int longestSubarray(vector<int>& nums, int limit) {
        int i = 0, j;
        int res = 1;
        multiset<int> m;
        for (j = 0; j < nums.size(); ++j) {
            m.insert(nums[j]);
            if (*m.rbegin() - *m.begin() > limit)
                m.erase(m.find(nums[i++]));
            res = max(res, j - i + 1);
        }
        return res;
    }
};