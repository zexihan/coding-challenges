class Solution {
private: 
    bool isPalindrome(string& s, int l, int r) {
        while (l < r) {
            if (s[l] != s[r])
                return false;
            l++;
            r--;
        }
        return true;
    }
    
    void helper(int start, string& s, vector<string>& path, vector<vector<string>>& res) {
        if (start == s.length()) {
            res.push_back(path);
            return;
        }
        
        for (int end = start; end < s.length(); end++) {
            if (isPalindrome(s, start, end)) {
                path.push_back(s.substr(start, end - start + 1));
                helper(end + 1, s, path, res);
                path.pop_back();
            }
        }
    }
    
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<string> path;
        helper(0, s, path, res);
        return res;
    }
};