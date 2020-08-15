// Two pointers
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int trap(vector<int>& height) {
        if (height.empty()) return 0;
        int n = height.size();
        int l = 0, r = n - 1;
        int lmax = height[0], rmax = height[n - 1];
        int res = 0;
        while (l <= r) {
            lmax = max(lmax, height[l]);
            rmax = max(rmax, height[r]);
            
            if (lmax < rmax) {
                res += lmax - height[l];
                l++;
            } else {
                res += rmax - height[r];
                r--;
            }
        }
        return res;
    }
};