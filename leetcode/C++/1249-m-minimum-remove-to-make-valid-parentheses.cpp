// Stack
// Time: O(n)
// Space: O(n)
class Solution {
public:
    string minRemoveToMakeValid(string s) {
        stack<int> sk;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] == '(') {
                sk.push(i);
            } else if (s[i] == ')') {
                if (sk.empty()) {
                   s[i] = '*';
                } else {
                    sk.pop();
                }
            }
        }
        
        while (!sk.empty()) {
            s[sk.top()] = '*';
            sk.pop();
        }
        
        string res;
        for (int i = 0; i < s.length(); ++i) {
            if (s[i] != '*') {
                res.push_back(s[i]);
            }
        }
        return res;
    }
};