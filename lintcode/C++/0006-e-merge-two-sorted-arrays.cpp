class Solution {
public:
    vector<int> mergeSortedArray(vector<int> &A, vector<int> &B) {
        vector<int> result;
        int i = 0, j = 0;
        while (i < A.size() && j < B.size()) {
            if (A[i] < B[j])
                result.push_back(A[i++]);
            else
                result.push_back(B[j++]);
        }

        while (i < A.size())
            result.push_back(A[i++]);
        
        while (j < B.size())
            result.push_back(B[j++]);
        
        return result;
    }
};