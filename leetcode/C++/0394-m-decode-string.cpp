class Solution {
private:
    string helper(string s, int& pos) {
        int num = 0;
        string word = "";
        for (; pos < s.length(); pos++) {
            char c = s[pos];
            if (c == '[') {
                string cur = helper(s, ++pos);
                for (;num > 0; num--)
                    word += cur;
            } else if (c >= '0' && c <= '9') {
                num = 10 * num + (c - '0');
            } else if (c == ']') {
                return word;
            } else {
                word += c;
            }
        }
        return word;
    }
    
public:
    string decodeString(string s) {
        int pos = 0;
        return helper(s, pos);
    }
};