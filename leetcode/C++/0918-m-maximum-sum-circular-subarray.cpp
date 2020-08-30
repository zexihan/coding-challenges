class Solution {
public:
    int maxSubarraySumCircular(vector<int>& A) {
        int n = A.size();
        if (n == 0) return 0;
        int maxSoFar = A[0];
        int maxTotal = A[0];
        int minSoFar = A[0];
        int minTotal = A[0];
        int sum = A[0];
        for (int i = 1; i < n; i++) {
            maxSoFar = max(A[i], maxSoFar + A[i]);
            maxTotal = max(maxTotal, maxSoFar);
            
            minSoFar = min(A[i], minSoFar + A[i]);
            minTotal = min(minTotal, minSoFar);
            
            sum += A[i];
        }
        
        if (sum == minTotal) return maxTotal;
        return max(maxTotal, sum - minTotal);
    }
};