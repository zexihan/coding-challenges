// Time: O(n)
// Space: O(n)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> left(n, 1);
        vector<int> right(n, 1);
        vector<int> res;
        
        for (int i = 1; i < n; i++) {
            left[i] = nums[i - 1] * left[i - 1];
            right[n - i - 1] = nums[n - i] * right[n - i];
        }
        for (int i = 0; i < n; i++) {
            res.push_back(left[i] * right[i]);
        }
        return res;
    }
};


// Time: O(n)
// Space: O(1)
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int n = nums.size();
        vector<int> res(n, 1);
        
        for (int i = 1; i < n; i++) {
            res[i] = nums[i - 1] * res[i - 1];
        }
        int right = 1;
        for (int i = n - 1; i > -1; i--) {
            res[i] *= right;
            right *= nums[i];
        }
        return res;
    }
};