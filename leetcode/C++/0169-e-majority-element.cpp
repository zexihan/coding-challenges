// Hash Map
// Time: O(n)
// Space: O(n)
class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counter;
        for (int num : nums) {
            if (counter.find(num) == counter.end()) {
                counter[num] = 1;  
            } else {
                counter[num]++;
            }
        }
        int res;
        int mj_cnt = 0;
        auto map_it = counter.cbegin();
        while (map_it != counter.cend()) {
            if (map_it->second > mj_cnt) {
                mj_cnt = map_it->second;
                res = map_it->first;
            }
            map_it++;
        }
        return res;
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