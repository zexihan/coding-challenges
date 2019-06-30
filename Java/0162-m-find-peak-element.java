/* 
Binary Search
*/
class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0, end = nums.length - 1;
        int mid;
        while (start + 1 < end) {
            mid = start + (end - start) / 2;
            if (nums[mid] < nums[mid - 1])
                end = mid;
            else if (nums[mid] < nums[mid + 1])
                start = mid;
            else
                return mid;
        }
        if (nums[start] < nums[end])
            return end;
        return start;
    }
}