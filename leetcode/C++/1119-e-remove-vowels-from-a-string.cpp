class Solution {
public:
    string removeVowels(string S) {
        string res;
        for (char c : S) {
            if (c != 'a' && c != 'e' && c != 'i' && c != 'o' && c!= 'u')
                res.push_back(c);
        }
        return res;
    }
};