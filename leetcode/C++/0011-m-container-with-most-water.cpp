class Solution {
public:
    int maxArea(vector<int>& height) {
        int i = 0, j = height.size() - 1;
        int cur = 0, res = 0;
        while (i < j) {
            cur = (j - i) * min(height[i], height[j]);
            res = max(cur, res);
            if (height[i] < height[j])
                i++;
            else
                j--;
        }
        return res;
    }
};