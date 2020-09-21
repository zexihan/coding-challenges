class Solution {
private: 
    bool helper(string& s, string& t, int si, int ti) {
        for (; si < s.length(); si++, ti++) {
            if (s[si] != t[ti])
                return false;
        }
        return true;
    }
    
public:
    bool isOneEditDistance(string s, string t) {
        int sLen = s.length();
        int tLen = t.length();
        if (tLen < sLen) return isOneEditDistance(t, s);
        if (tLen - sLen > 1) return false;
        for (int i = 0; i < sLen; i++) {
            if (s[i] != t[i]) {
                if (sLen == tLen)
                    return helper(s, t, i+1, i+1);
                else
                    return helper(s, t, i, i+1);
            }
        }
        return sLen+1 == tLen;
    }
};