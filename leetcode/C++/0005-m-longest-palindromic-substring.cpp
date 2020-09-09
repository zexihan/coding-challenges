class Solution {
public:
    string longestPalindrome(string s) {
        int lo = 0, maxLen = 0;
        if (s.length() < 2)
            return s;

        for (int i = 0; i < s.length(); i++) {
            extendPalindrome(s, i, i, lo, maxLen);
            extendPalindrome(s, i, i+1, lo, maxLen);
        }
        return s.substr(lo, maxLen);
    }

    void extendPalindrome(string s, int j, int k, int& lo, int& maxLen) {
        while (j >= 0 && k < s.length() && s[j] == s[k]) {
            j--;
            k++;
        }
            
        if (maxLen < k - j - 1) {
            lo = j + 1;
            maxLen = k - j -1;
        }
    }
};