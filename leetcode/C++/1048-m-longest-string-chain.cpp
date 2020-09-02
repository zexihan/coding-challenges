// DP + HashMap
class Solution {
public:
    int longestStrChain(vector<string>& words) {
        sort(words.begin(), words.end(), [](string& a, string& b){
            return a.length() < b.length();
        });
        unordered_map<string, int> dp;
        for (string w : words)
            dp[w] = 1;
        int res = 0;
        for (string w : words) {
            for (int i = 0; i < w.length(); i++) {
                string pre = w.substr(0, i) + w.substr(i + 1);
                if (dp.find(pre) != dp.end())
                    dp[w] = max(dp[w], dp[pre] + 1);
            }
            res = max(res, dp[w]);
        }
        return res;
    }
};