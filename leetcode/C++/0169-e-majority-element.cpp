// Hash Map
// Time: O(n)
// Space: O(n)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;
        int majority = 0, cnt = 0;
        for (int num : nums) {
            ++counts[num];
            if (counts[num] > cnt) {
                majority = num;
                cnt = counts[num];
            }
        }
        return majority;
    }
};

// Moore Voting
// Time: O(n)
// Space: O(1)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0;
        int candidate;
        
        for (int num : nums) {
            if (count == 0) {
                candidate = num;
            }
            count += (num == candidate) ? 1 : -1;
        }
        return candidate;
    }
};