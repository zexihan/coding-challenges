class Solution {
public:
    string removeDuplicates(string s, int k) {
        vector<pair<char, int>> stk;
        for (int i = 0; i < s.length(); i++) {
            if (stk.size() && stk.back().first == s[i]) {
                if (stk.back().second + 1 == k)
                    stk.pop_back();
                else
                    stk.back().second++;
            } else
                stk.push_back({s[i], 1});
        }
        string res;
        for (auto p : stk)
            res += string(p.second, p.first);
        return res;
    }
};