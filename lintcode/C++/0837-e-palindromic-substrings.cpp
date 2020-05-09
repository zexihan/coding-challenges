// 考虑如果substring(i,j)如果是回文串，那么str[i]和str[j]一定相同，并且一定满足以下两个条件之一
// 1.substring(i+1,j-1)也是回文串
// 2.j-i<=2，即substring(i,j)长度<=2
// Time: O(n^2)
class Solution {
    public:
        int countPalindromicSubstrings(string &str) {
            int n = str.size();
            int ans = 0;
            vector<vector<int>> dp(n, vector<int> (n, 0));
            for (int i = 0; i < n; ++i) {
                for (int j = 0; j <= i; ++j) {
                    dp[i][j] = (str[j] == str[i]) && (i - j <= 2 || dp[i - 1][j + 1]);
                    ans += dp[i][j];
                }
            }
            return ans;
        }
};