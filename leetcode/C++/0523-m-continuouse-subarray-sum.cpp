// Brute force
// Time: O(n^2)
// Space: O(1)
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int n = nums.size();
        for (int i = 0; i < n - 1; i++) {
            int curSum = nums[i];
            for (int j = i + 1; j < n; j++) {
                curSum += nums[j];
                if ((k == 0 && curSum == 0) || 
                    (k != 0 && curSum % k == 0))
                    return true;
            }
        }
        return false;
    }
};

// Math, Hash Map
// a % k = x
// b % k = x
// (a - b) % k = x - x = 0
// here a - b = the sum between i and j.
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool checkSubarraySum(vector<int>& nums, int k) {
        int sum = 0;
        unordered_map<int, int> hm;
        hm[0] = -1;
        for (int i = 0; i < nums.size(); i++) {
            sum += nums[i];
            if (k != 0)
                sum = sum % k;
            if (hm.find(sum) != hm.end()) {
                if (i - hm[sum] > 1)
                    return true;
            } else
                hm[sum] = i;
        }
        return false;
    }
};