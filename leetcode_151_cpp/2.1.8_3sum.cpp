class Solution {
    public:
        vector<vector<int>> threeSum(vector<int> &nums) {
            vector<vector<int>> result;
            if (nums.size() < 3)
                return result;
            sort(nums.begin(), nums.end());
            const int target = 0;

            auto last = nums.end();
            for (auto i = nums.begin(); i < last - 2; ++i) {
                auto j = i + 1;
                if (i > nums.begin() && *i == *(i - 1))
                    continue;
                auto k = last - 1;
                while (j < k) {
                    if (*i + *j + *k < target) {
                        ++j;
                        while (*j == *(j-i) && j < k)
                            ++j;
                    } else if (*i + *j + *k > target) {
                        --k;
                        while (*k == *(k + i) && j < k)
                            --k;
                    } else {
                        result.push_back({*i, *j, *k});
                        ++j;
                        --k;
                        while (*j == *(j - i) && *k == *(k + i) && j < k)
                            ++j;
                    }
                }
            }
            return result;
        }
};