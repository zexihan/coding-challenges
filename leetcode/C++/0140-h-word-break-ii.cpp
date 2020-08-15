// Recursion with memorization, TLE
class Solution {
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        set<string> words(wordDict.begin(), wordDict.end());
        unordered_map<string, vector<string>> mem;
        return breakW(s, mem, words);
    }

    vector<string> breakW(string s, unordered_map<string, vector<string>> mem, set<string> words) {
        if (mem.find(s) != mem.end())
            return mem[s];
        
        vector<string> res;
        if (words.find(s) != words.end())
            res.push_back(s);
        for (int i = 1; i < s.length(); i++) {
            string left = s.substr(0, i);
            string right = s.substr(i, s.length() - i);
            if (words.find(right) == words.end())
                continue;
            vector<string> rem = breakW(left, mem, words);
            for (string w : rem)
                res.push_back(w + " " + right);
        }
        mem[s] = res;
        return mem[s];
    }
};