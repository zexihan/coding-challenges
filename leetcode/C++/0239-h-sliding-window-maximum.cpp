// Deque
// Time: O(n)
// Space: O(n)
class Solution {
public:
    vector<int> maxSlidingWindow(vector<int>& nums, int k) {
        vector<int> res;
        // monotone decreasing deque
        deque<int> dq;
        for (int i = 0; i < nums.size(); i++) {
            // pop back before insertion
            while (!dq.empty() && nums[i] > dq.back()) 
                dq.pop_back();
            dq.push_back(nums[i]);
            if (i >= k - 1) {
                res.push_back(dq.front());
                // pop front before window moves
                if (dq.front() == nums[i - k + 1]) 
                    dq.pop_front();
            }
        }
        return res;
    }
};