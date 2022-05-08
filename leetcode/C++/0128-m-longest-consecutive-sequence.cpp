class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if (!nums.size())
            return 0;
        
        unordered_map<int, int> map;
        int max_length = 1;
        int left = 0;
        int right = 0;
        for (auto num : nums) {
            if (map.find(num) != map.end()) continue;
            
            if (map.find(num - 1) != map.end())
                left = map[num - 1];
            else
                left = 0;
            
            if (map.find(num + 1) != map.end())
                right = map[num + 1];
            else
                right = 0;
            
            int cur_length = 1 + left + right;
            max_length = max(max_length, cur_length);

            map[num] = cur_length;
            map[num - left] = cur_length;
            map[num + right] = cur_length;
        }
        return max_length;
    }
};