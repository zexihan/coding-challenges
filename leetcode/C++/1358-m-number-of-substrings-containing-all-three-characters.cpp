// Two pointers
class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.length();
        if (n < 3) return 0;
        vector<int> letters(3, 0);
        int count = 0, res = 0;
        int i = 0, j = 0;
        while (i <= j && j < n) {
            while (j < n && count < 3) {
                if (letters[s[j] - 'a'] == 0)
                    count++;
                letters[s[j] - 'a']++;
                j++;
            }
            if (count == 3)
                res += n - j + 1;
            if (letters[s[i] - 'a'] == 1)
                count--;
            letters[s[i] - 'a']--;
            i++;
        }
        while (i < j && count == 3) {
            res++;
            if (letters[s[i] - 'a'] == 1)
                count--;
            letters[s[i] - 'a']--;
            i++;
        }
        return res;
    }
};