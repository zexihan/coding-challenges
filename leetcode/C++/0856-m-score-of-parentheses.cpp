class Solution {
public:
    int scoreOfParentheses(string S) {
        stack<int> stk;
        stk.push(0); // the score of the current frames
        for (char c : S) {
            if (c == '(') {
                stk.push(0);
            } else {
                int v = stk.top();
                stk.pop();
                int w = stk.top();
                stk.pop();
                stk.push(w + max(2 * v, 1));
            }
        }
        return stk.top();
    }
};