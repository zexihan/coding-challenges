class Solution {
public:
    int twoSumLessThanK(vector<int>& A, int K) {
        sort(A.begin(), A.end());
        int i = 0, j = A.size() - 1;
        int sum, res = -1;
        while (i < j) {
            sum = A[i] + A[j];
            if (sum < K) {
                i++;
                res = max(res, sum);
            } else {
                j--;
            }
        }
        return res;
    }
};