class Solution {
private:
    void revWord(int l, int r, vector<char>& s) {
        while (l <= r) {
            swap(s[l], s[r]);
            l++, r--;
        }
    }
    
public:
    void reverseWords(vector<char>& s) {
        reverse(s.begin(), s.end());
        int i = 0, j = 0;
        int n = s.size();
        while (i <= j && j < n) {
            while (j < n && s[j] != ' ') {
                j++;
            }
            revWord(i, j - 1, s);
            i = j + 1;
            j++;
        }
    }
};