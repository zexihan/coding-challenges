// Hash Table
// Time: O(n)
// Space: O(n)
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> counter;
        for (int num : nums) {
            if (counter.find(num) != counter.end())
                return true;
            counter.insert(num);
        }
        return false;
    }
};