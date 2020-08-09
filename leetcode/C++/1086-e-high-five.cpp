class Solution {
public:
    vector<vector<int>> highFive(vector<vector<int>>& items) {
        map<int, vector<int>> scores;
        for (int i = 0; i < items.size(); ++i) {
            if (scores.find(items[i][0]) == scores.end()) {
                scores[items[i][0]] = vector<int>{items[i][1]};
            } else {
                scores[items[i][0]].push_back(items[i][1]);
            }
        }
        
        vector<vector<int>> res;
        auto map_it = scores.begin();
        while(map_it != scores.end()) {
            int curSum = 0;
            sort(map_it->second.begin(), map_it->second.end(), greater<int>());
            for (int i = 0; i < 5; ++i) {
                curSum += map_it->second[i];
            }
            res.push_back(vector<int>{map_it->first, curSum / 5});
            map_it++;
        }
        return res;
    }
};