class Solution {
public:
    int subarraysDivByK(vector<int>& A, int K) {
        int n = A.size();
        vector<int> p(n+1, 0);
        for (int i = 0; i < n; i++)
            p[i+1] = p[i] + A[i];
        // (p[j] - p[i]) % K == 0 <=> p[j] % K == p[i] % K
        vector<int> count(K, 0);
        for (int x : p)
            count[(x % K + K) % K]++;
        
        int res = 0;
        for (int v : count)
            res += v * (v - 1) / 2;
        return res;
    }
};