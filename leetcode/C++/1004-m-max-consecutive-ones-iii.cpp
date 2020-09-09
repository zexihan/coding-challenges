class Solution {
public:
    int longestOnes(vector<int>& A, int K) {
        int n = A.size();
        int i = 0, j = 0;
        while (j < n) { 
            if (A[j] == 0)
                K--;
            if (K < 0) { 
                if (A[i] == 0)
                    K++;
                i++;
            }
            j++;
        }
        return (j - i);
    }
};