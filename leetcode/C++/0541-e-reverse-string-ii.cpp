class Solution {
public:
    string reverseStr(string s, int k) {
        int n = s.length();
        for (int left = 0; left < n; left += 2 * k) {
            for (int i = left, j = min(left + k - 1, n - 1); i < j; i++, j--) {
                swap(s[i], s[j]);
            }
        }
        return s;
    }
};