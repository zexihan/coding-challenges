// DP
// G(n): the number of unique BST for a sequence of length n
// F(i, n): the number of unique BST, where the number i is served as the root of BST (1 <= i <=n)
// 1. G(n) = \sum_{i=1}^{n}F(i, n)
// 2. F(i, n) = G(i - 1)G(n - i)
// Combining 1 and 2, G(n) = \sum_{i=1}^{n}G(i - 1)G(n - i)
class Solution {
public:
    int numTrees(int n) {
        vector<int> G(n+1);
        G[0] = 1;
        G[1] = 1;
        
        for (int i = 2; i <=n; i++)
            for (int j = 1; j <= i; j++)
                G[i] += G[j - 1] * G[i - j];
        return G[n];
    }
};