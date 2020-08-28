class Solution {
private:
    int helper(vector<int>& A, int L, int M) {
        int n = A.size();
        vector<int> left(n + 1), right(n + 1);
        int res = INT_MIN;
        for (int i = 0, j = n - 1, l_sum = 0, r_sum = 0; i < n; i++, j--) {
            l_sum += A[i], r_sum += A[j];
            left[i + 1] = max(left[i], l_sum);
            right[j] = max(right[j + 1], r_sum);
            if (i + 1 >= L) l_sum -= A[i - L + 1];
            if (i + 1 >= M) r_sum -= A[j + M - 1];
        }
        for (int i = 0; i < A.size(); i++)
            res = max(res, left[i] + right[i]);
        return res;
    }
    
public:
    int maxSumTwoNoOverlap(vector<int>& A, int L, int M) {
        return max(helper(A, L, M), helper(A, M, L));
    }
};