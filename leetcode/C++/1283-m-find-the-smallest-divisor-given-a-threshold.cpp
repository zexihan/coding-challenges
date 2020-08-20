class Solution {
public:
    int smallestDivisor(vector<int>& nums, int threshold) {
        int l = 1, r = 1e6;
        sort(nums.begin(), nums.end());
        while (l < r) {
            int sum = 0;
            int mid = l + (r - l) / 2;
            for (int num : nums) 
                sum += (num + mid - 1) / mid;
            if (sum > threshold)
                l = mid + 1;
            else
                r = mid;
        }
        return l;
    }
};