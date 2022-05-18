// Time: O(nlog(min(n, k)))
// Space: O(min(n, k))
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        set<int> window;
        for (int i = 0; i < nums.size(); ++i) {
            if (i > k && i - k - 1 < nums.size()) 
                window.erase(nums[i - k - 1]);
            auto it = window.lower_bound(max(nums[i], INT_MIN + t) - t);
            if (it != window.end() && *it <= min(nums[i], INT_MAX - t) + t) 
                return true;
            window.insert(nums[i]);
        }
        return false;
    }
};