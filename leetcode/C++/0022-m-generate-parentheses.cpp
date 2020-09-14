// Backtracking
class Solution {
private:
    void helper(int n, int open, int close, string& path, vector<string>& res) {
        if (open == n && close == n) {
            res.push_back(path);
            return;
        }
        if (open < n) {
            path += "(";
            helper(n, open + 1, close, path, res);
            path.pop_back();
        }
            
        if (close < open) {
            path += ")";
            helper(n, open, close + 1, path, res);
            path.pop_back();
        }
    }
    
public:
    vector<string> generateParenthesis(int n) {
        string path = "";
        vector<string> res;
        helper(n, 0, 0, path, res);
        return res;
    }
};