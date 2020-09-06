class Solution {
public:
    int lengthOfLongestSubstringKDistinct(string s, int k) {
        int n = s.length();
        vector<int> letters(256, 0);
        int i = 0, j = 0;
        int count = 0, res = 0;
        while (i <= j && j < n) {
            while (count <= k && j < n) {
                if (letters[(int)s[j]] == 0) {
                    if (count == k)
                        break;
                    count++;
                }
                letters[(int)s[j]]++;
                j++;
            }
            res = max(res, j - i);
            if (letters[(int)s[i]] == 1)
                count--;
            letters[(int)s[i]]--;
            i++;
        }
        return res;
    }
};