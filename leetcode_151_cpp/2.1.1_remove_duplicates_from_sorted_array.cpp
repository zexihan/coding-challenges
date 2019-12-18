class Solution {
public:
    int removeDuplicates(vector<int>& nums) 
    {
        if (nums.empty())
            return 0;
        int index = 0;
        for (int i = 1; i < nums.size(); i++)
        {
            if (nums[index] != nums[i])
                nums[++index] = nums[i];
        }
        return index + 1;
    }

    int removeDuplicates_2(vector<int>& nums) 
    {
        if (nums.empty())
            return 0;
        vector<int>::iterator iter1 = nums.begin();
        vector<int>::iterator iter2 = nums.begin() + 1;
        for ( ; iter2 != nums.end(); ++iter2)
        {
            if (*iter1 != *iter2)
                *(++iter1) = *iter2;
        }
        return iter1 - nums.begin() + 1;
    }
}