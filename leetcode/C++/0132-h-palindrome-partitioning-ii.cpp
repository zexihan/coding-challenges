// DP
// Time: O(N^2)
// Space: O(N^2)
class Solution {
private: 
    vector<vector<bool>> calcPalin(string& s) {
        int n = s.length();
        vector<vector<bool>> f(n, vector<bool>(n, false));
        int i, j, c;
        // odd length
        // center charactor
        for (c = 0; c < n; ++c) {
            i = c, j = c;
            // extend to both directions
            while (i >= 0 && j < n && s[i] == s[j]) {
                f[i][j] = true;
                --i, ++j;
            }
        }
        // even length
        // center line
        for (c = 0; c < n - 1; ++c) {
            i = c, j = c + 1;
            // extend to both directions
            while (i >= 0 && j < n && s[i] == s[j]) {
                f[i][j] = true;
                --i, ++j;
            }
        }
        return f;
    }
    
public:
    int minCut(string s) {
        int n = s.length();
        if (n == 0) return 0;
        vector<vector<bool>> isPalin = calcPalin(s);
        int i, j;
        vector<int> f(n + 1, INT_MAX);
        f[0] = 0;
        for (i = 1; i <= n; ++i) {
            for (j = 0; j < i; ++j) {
                if (isPalin[j][i-1])
                    f[i] = min(f[i], f[j] + 1);
            }
        }
        return f[n] - 1;
    }
};