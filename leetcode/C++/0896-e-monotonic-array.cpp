class Solution {
public:
    bool isMonotonic(vector<int>& A) {
        bool incre = true, decre = true;
        for (int i = 0; i < A.size() - 1; i++) {
            if (A[i] > A[i+1])
                incre = false;
            if (A[i] < A[i+1])
                decre = false;
        }
        return incre || decre;
    }
};