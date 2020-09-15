// Recursion and memorization
class Solution {
private:
    bool helper(string& s, unordered_set<string>& wordSet, int start, vector<int>& memo) {
        if (start == s.size()) return true;
        if (memo[start] != -1) return memo[start];
        for (int end = start + 1; end <= s.length(); end++) {
            string sub = s.substr(start, end - start);
            if (wordSet.find(sub) != wordSet.end() && helper(s, wordSet, end, memo)) {
                return memo[start] = 1;
            }
        }
        return memo[start] = 0;
    }
    
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        unordered_set<string> wordSet(wordDict.begin(), wordDict.end());
        vector<int> memo(s.length(), -1);
        return helper(s, wordSet, 0, memo);
    }
};