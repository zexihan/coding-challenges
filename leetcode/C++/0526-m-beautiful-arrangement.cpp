// Backtracking
class Solution {
private:
    void helper(int N, int cur, vector<bool>& visited, int& res) {
        if (cur > N) {
            res++;
            return;
        }
        for (int i = 1; i <= N; i++) {
            if (!visited[i] && (cur % i == 0 || i % cur == 0)) {
                visited[i] = true;
                helper(N, cur + 1, visited, res);
                visited[i] = false;
            }
        }
    }

public:
    int countArrangement(int N) {
        vector<bool> visited(N+1, false);
        int res = 0;
        helper(N, 1, visited, res);
        return res;
    }
};