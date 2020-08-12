// Two pointers
// Time: O(NlogN)
// Space: O(1)
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int p = 0, q = 1;
        int count = 0;
        while (p < nums.size() && q < nums.size()) {
            int diff = nums[q] - nums[p];
            if (diff < k || p == q)
                q++;
            else if (diff > k)
                p++;
            else {
                p++;
                count++;
                while (p < nums.size() && nums[p] == nums[p - 1])
                    p++;
            }
        }
        return count;
    }
};

// Hash table
// Time: O(N)
// Space: O(N)
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int res = 0;
        unordered_map<int, int> counter;
        for (int n : nums)
            counter[n]++;
        auto map_it = counter.begin();
        while (map_it != counter.end()) {
            int x = map_it->first, f = map_it->second;
            if (k > 0 && counter.find(x + k) != counter.end())
                res++;
            else if (k == 0 && f > 1)
                res++;
            map_it++;
        }
        return res;
    }
};