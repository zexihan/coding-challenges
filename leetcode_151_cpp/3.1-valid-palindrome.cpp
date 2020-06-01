// Time: O(n)
// Space: O(1)
class Solution {
public:
    bool isPalindrome(string s) {
        transform(s.begin(), s.end(), s.begin(),
                  [](unsigned char c) { return tolower(c); });
        auto left = s.begin(), right = prev(s.end());
        while (left < right) {
            if (!isalnum(*left)) ++left;
            else if (!isalnum(*right)) --right;
            else if (*left != *right) return false;
            else {left++, right--;}
        }
        return true;
    }
};