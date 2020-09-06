// Two pointers
class Solution {
public:
    int lengthOfLongestSubstringTwoDistinct(string s) {
        int n = s.length();
        vector<int> letters(256, 0);
        int i = 0, j = 0;
        int count = 0, res = 0;
        while (i <= j && j < n) {
            while (count <= 2 && j < n) {
                if (letters[(int)s[j]] == 0)
                    count++;
                letters[(int)s[j]]++;
                if (count <= 2)
                    res = max(res, j - i + 1);
                j++;
            }
            if (letters[(int)s[i]] == 1)
                count--;
            letters[(int)s[i]]--;
            i++;
        }
        return res;
    }
};