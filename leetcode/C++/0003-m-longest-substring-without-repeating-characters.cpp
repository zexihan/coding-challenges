// Two pointers
class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int n = s.length();
        vector<int> letters(256, 0);
        int res = 0;
        int i = 0, j = 0;
        while (i <= j && j < n) {
            while (letters[(int)s[j]] == 0 && j < n) {
                letters[(int)s[j]]++;
                j++;
            }
            res = max(res, j - i);
            letters[(int)s[i]]--;
            i++;
        }
        return res;
    }
};