// DP
// 定义三维数组dp，其中dp[i][j][k]表示在前i个字符串中，使用j个0和 k个1的情况下最多可以得到的字符串数量。
// 假设数组str的长度为l，则最终答案为dp[l][m][n]。
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int l = strs.size();
        vector<vector<vector<int>>> dp(l + 1, vector<vector<int>>(m + 1, vector<int>(n + 1)));
        for (int i = 1; i <= l; i++) {
            vector<int>&& zerosOnes = getZerosOnes(strs[i - 1]);
            int zeros = zerosOnes[0], ones = zerosOnes[1];
            for (int j = 0; j <= m; j++) {
                for (int k = 0; k <= n; k++) {
                    dp[i][j][k] = dp[i - 1][j][k];
                    if (j >= zeros && k >= ones) {
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - zeros][k - ones] + 1);
                    }
                }
            }
        }
        return dp[l][m][n];
    }

    vector<int> getZerosOnes(string& str) {
        vector<int> zerosOnes(2);
        int l = str.length();
        for (int i = 0; i < l; i++) {
            zerosOnes[str[i] - '0']++;
        }
        return zerosOnes;
    }
};

// Time: O(lmn + L)
// Space: O(mn)
class Solution {
public:
    int findMaxForm(vector<string>& strs, int m, int n) {
        int length = strs.size();
        vector<vector<int>> dp(m + 1, vector<int>(n + 1));
        for (int i = 0; i < length; i++) {
            vector<int>&& zerosOnes = getZerosOnes(strs[i]);
            int zeros = zerosOnes[0], ones = zerosOnes[1];
            for (int j = m; j >= zeros; j--) {
                for (int k = n; k >= ones; k--) {
                    dp[j][k] = max(dp[j][k], dp[j - zeros][k - ones] + 1);
                }
            }
        }
        return dp[m][n];
    }

    vector<int> getZerosOnes(string& str) {
        vector<int> zerosOnes(2);
        int length = str.length();
        for (int i = 0; i < length; i++) {
            zerosOnes[str[i] - '0']++;
        }
        return zerosOnes;
    }
};

