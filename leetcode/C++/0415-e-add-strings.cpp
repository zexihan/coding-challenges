class Solution {
public:
    string addStrings(string num1, string num2) {
        int a = 0, b = 0;
        int sum = 0, carry = 0;
        string res;
        int i = num1.length() - 1, j = num2.length() - 1;
        while (i > -1 || j > -1) {
            a = i > -1 ? num1[i] - '0' : 0;
            b = j > -1 ? num2[j] - '0' : 0;
            sum = (a + b + carry) % 10;
            carry = (a + b + carry) / 10;
            res += to_string(sum);
            i--, j--;
        }
        
        if (carry != 0)
            res.push_back('1');
        
        reverse(res.begin(), res.end());
        
        return res;
    }
};