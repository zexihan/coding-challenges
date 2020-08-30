class Solution {
public:
    int findJudge(int N, vector<vector<int>>& trust) {
        if (trust.size() < N - 1)
            return -1;
        
        vector<int> trustScores(N + 1, 0);
        
        for (auto relation : trust) {
            trustScores[relation[0]]--;
            trustScores[relation[1]]++;
        }
        
        for (int i = 1; i <= N; i++)
            if (trustScores[i] == N - 1)
                return i;
        return -1;
    }
};