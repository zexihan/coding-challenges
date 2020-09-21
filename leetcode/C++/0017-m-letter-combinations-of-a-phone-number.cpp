// Backtracking
class Solution {
private:
    void helper(string& digits, unordered_map<char, string>& mp, int pos, 
                string& path, vector<string>& res) {
        if (path.length() == digits.length()) {
            res.push_back(path);
            return;
        }
        string candidates = mp[digits[pos]];
        for (int i = 0; i < candidates.length(); i++) {
            path.push_back(candidates[i]);
            helper(digits, mp, pos+1, path, res);
            path.pop_back();
        }
    }
    
public:
    vector<string> letterCombinations(string digits) {
        vector<string> res;
        if (!digits.length()) return res;
        unordered_map<char, string> mp = {
            {'2', "abc"}, {'3', "def"}, {'4', "ghi"},
            {'5', "jkl"}, {'6', "mno"}, {'7', "pqrs"},
            {'8', "tuv"}, {'9', "wxyz"}};
        string path = "";
        helper(digits, mp, 0, path, res);
        return res;
    }
};