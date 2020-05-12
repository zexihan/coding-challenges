class Solution {
public:
    bool compareStrings(string A, string B) {
        int count[26];
        for (int i = 0; i < 26; i++) 
            count[i] = 0;
        for (int i = 0; i < A.length(); i++) 
            count[A[i] - 'A']++;
        for (int i = 0; i < B.length(); i++) {
            count[B[i] - 'A']--;
            if (count[B[i] - 'A'] < 0) 
                return false;
        }
        return true;
    }
};