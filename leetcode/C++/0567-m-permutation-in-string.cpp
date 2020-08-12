// Sliding window
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        int m = s1.length(), n = s2.length();
        if (m > n) return false;
        vector<int> s1Counter(26, 0);
        vector<int> s2Counter(26, 0);
        for (int i = 0; i < m; i++) {
            s1Counter[s1[i] - 'a']++;
            s2Counter[s2[i] - 'a']++;
        }
        for (int i = 0; i < n - m; i++) {
            if (s1Counter == s2Counter)
                return true;
            s2Counter[s2[i] - 'a']--;
            s2Counter[s2[i + m] - 'a']++;
        }
        return s1Counter == s2Counter;
    }
};