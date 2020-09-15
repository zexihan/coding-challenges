class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs) {
            string s2 = s;
            sort(s2.begin(), s2.end());
            mp[s2].push_back(s);
        }
        vector<vector<string> > res;
        for(auto item : mp) res.push_back(item.second);
        return res;
    }
};


class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        vector<vector<string>> res;
        unordered_map<string, vector<string>> mp;
        for (string s : strs) {
            vector<int> count(26, 0);
            for (char c : s) {
                count[c - 'a']++;
            }
            string code = "";
            for (int c : count)
                code += "#" + to_string(c);
            mp[code].push_back(s);
        }
        for (auto it = mp.begin(); it != mp.end(); it++) {
            res.push_back(it->second);
        }
        return res;
    }
};