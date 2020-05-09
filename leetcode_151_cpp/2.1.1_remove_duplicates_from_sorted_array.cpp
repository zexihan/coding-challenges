/*
Time: O(n)
Space: O(1)
*/
class Solution {
    public:
        int removeDuplicates(vector<int>& nums) {
            if (nums.empty())
                return 0;
            int index = 0;
            for (int i = 1; i < nums.size(); i++) {
                if (nums[index] != nums[i])
                    nums[++index] = nums[i];
            }
            return index + 1;
        }
};

// Use iterator
// Time: O(n)
// Space: O(1)
class Solution {
    public:
        int removeDuplicates(vector<int> &nums) {
            if (nums.empty())
                return 0;
            vector<int>::iterator iter1 = nums.begin();
            vector<int>::iterator iter2 = nums.begin() + 1;
            for (; iter2 != nums.end(); ++iter2) {
                if (*iter1 != *iter2)
                    *(++iter1) = *iter2;
            }
            return iter1 - nums.begin() + 1;
        }
};

// Use STL
// Time: O(n)
// Space: O(1)
class Solution {
    public:
        int removeDuplicates(vector<int> &nums) {
            return distance(nums.begin(), unique(nums.begin(), nums.end()));
        }
};

// Use STL
// Time: O(n)
// Space: O(1)
class Solution {
    public:
        int removeDuplicates(vector<int> &nums) {
            return distance(nums.begin(), removeDuplicates(nums.begin(), nums.end(), nums.begin()));
        }

        template<typename InIt, typename OutIt>
        OutIt removeDuplicates(InIt first, InIt last, OutIt output) {
            while (first != last) {
                *output++ = *first
                first = upper_bound(first, last, *first)
            }

            return output;
        }
};