class Solution {
public:
    int search(vector<int>& nums, int target) {
        if (nums.empty()) 
            return -1;
        
        int start = 0, end = nums.size() - 1;
        while (start + 1 < end) {
            const int mid = start + (end - start) / 2;
            if (nums[mid] >= nums[start]) {
                if (nums[mid] >= target && nums[start] <= target) 
                    end = mid;
                else 
                    start = mid;
            } else {
                if (nums[mid] <= target && nums[end] >= target) 
                    start = mid;
                else 
                    end = mid;
            }
        }
        
        if (nums[start] == target) 
            return start;
        if (nums[end] == target) 
            return end;
        
        return -1;
    }
};