// mono stack
// Time: O(m + n)
// Space: O(m + n)
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> stk;
        unordered_map<int, int> hm;
        for (int i = 0; i < nums2.size(); i++) {
            while (stk.size() && nums2[i] > stk.top()) {
                hm[stk.top()] = nums2[i];
                stk.pop();
            }
            stk.push(nums2[i]);
        }
        while (stk.size()) {
            hm[stk.top()] = -1;
            stk.pop();
        }
        vector<int> res;
        for (int i = 0; i < nums1.size(); i++) 
            res.push_back(hm[nums1[i]]);
        return res;
    }
};