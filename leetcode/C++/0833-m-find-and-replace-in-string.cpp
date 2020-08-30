class Solution {
public:
    string findReplaceString(string S, vector<int>& indexes, vector<string>& sources, vector<string>& targets) {
        map<int, pair<string, string>> mp;
        for (int i = 0; i < indexes.size(); i++)
            mp[indexes[i]] = {sources[i], targets[i]};
        
        int p = 0;
        string res;
        while (p < S.length()) {
            if (mp.find(p) != mp.end() && S.substr(p, mp[p].first.size()) == mp[p].first) {
                res += mp[p].second;
                p += mp[p].first.size();
            } else {
                res += S[p];
                p++;
            }
        }
        return res;
    }
};