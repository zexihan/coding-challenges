// Time: O(n)
class Solution_1 {
public:
    int findMin(vector<int>& nums) {
        if (nums.size() == 1)
            return nums[0];
        for (int i = 1; i < nums.size(); i++) {
            if (nums[i] < nums[i-1])
                return nums[i];
            else if (i == nums.size()-1)
                return nums[0];
        }
    }
};

//Time: O(logn)
class Solution_2 {
public:
    int findMin(vector<int>& nums) {
       int low = 0;
       int high = nums.size()-1;
       while (low < high-1) {
            if (nums[low] < nums[high])
                return nums[low];
            int mid = (low + high) / 2;
            if (nums[mid] > nums[low])
                low = mid;
            else
                high = mid; 
       }
       return min(nums[low], nums[high]);
    }
};