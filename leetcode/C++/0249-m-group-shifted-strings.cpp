class Solution {
private:
    string shiftEncode(string& s) {
        string code = "";
        for (int i = 0; i < s.length() - 1; i++) {
            int diff = s[i + 1] - s[i];
            if (diff < 0) diff += 26;
            code += 'a' + diff + ',';
        }
        return code;
    }

public:
    vector<vector<string>> groupStrings(vector<string>& strings) {
        map<string, vector<string>> mp;
        for (string s : strings) {
            mp[shiftEncode(s)].push_back(s);
        }
        vector<vector<string>> res;
        for (auto const& item : mp) {
            res.push_back(item.second);
        }
        return res;
    }
};