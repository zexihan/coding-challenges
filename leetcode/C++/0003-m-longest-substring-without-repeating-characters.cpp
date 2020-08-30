// Sliding window
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        set<char> st;
        int i = 0, j = 0, res = 0;
        while (i < n && j < n) {
            if (st.find(s[j]) == st.end()) {
                st.insert(s[j++]);
                res = max(res, j - i);
            } else {
                st.erase(s[i++]);
            }
        }
        return res;
    }
};


// Sliding window optimized
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length(), res = 0;
        vector<int> index(256); // current index of character
        // try to extend the range [i, j]
        for (int j = 0, i = 0; j < n; j++) {
            i = max(index[s[j]], i);
            res = max(res, j - i + 1);
            index[s[j]] = j + 1;
        }
        return res;
    }
};