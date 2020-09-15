class Solution {
public:
    bool isIdealPermutation(vector<int>& A) {
        // check A[i] > min(A[i+2:]
        int n = A.size();
        int floor = n;
        for (int i = n-1; i >= 2; i--) {
            floor = min(floor, A[i]);
            if (A[i-2] > floor) return false;
        }
        return true;
    }
};