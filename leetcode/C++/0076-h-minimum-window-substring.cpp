// Two pointers
class Solution {
public:
    string minWindow(string s, string t) {
        if (t.empty()) return "";
        int m = t.length(), n = s.length();
        vector<int> sLetters(256, 0);
        vector<int> tLetters(256, 0);
        int sCount = 0, tCount = 0;
        int start = 0, len = INT_MAX;
        for (int i = 0; i < m; i++) {
            if (tLetters[(int)t[i]] == 0)
                tCount++;
            tLetters[(int)t[i]]++;
        }
        
        int l = 0, r = 0;
        while (l <= r && l < n) {
            while (r < n && sCount < tCount) {
                sLetters[s[r]]++;
                if (sLetters[s[r]] == tLetters[s[r]]) {
                    sCount++;
                }
                r++;
            }
            if (sCount == tCount && r - l < len) {
                len = r - l;
                start = l;
            }
            if (sLetters[s[l]] == tLetters[s[l]])
                sCount--;
            sLetters[s[l]]--;
            l++;
        }
        if (len == INT_MAX)
            return "";
        return s.substr(start, len);
    }
};