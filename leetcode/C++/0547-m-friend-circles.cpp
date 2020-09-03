// DFS
class Solution {
private:
    void dfs(vector<vector<int>>& M, int cur, int n) {
        for (int i = 0; i < n; i++) {
            if (M[cur][i] == 1) {
                M[cur][i] = 0;
                M[i][cur] = 0;
                dfs(M, i, n);
            }
        }
    }
    
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (M[i][i] == 1) {
                res++;
                dfs(M, i, n);
            }
        }
        return res;
    }
};

// Union Find
class Solution {
public:
    int findCircleNum(vector<vector<int>>& M) {
        int n = M.size();
        vector<int> parent(n, -1);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (M[i][j] == 1 && i != j) {
                    union_op(parent, i, j);
                }
            }
        }
        int res = 0;
        for (int i = 0; i < n; i++) {
            if (parent[i] == -1) res++;
        }
        return res;
    }
    
    int find_parent(vector<int>& parent, int i) {
        vector<int> path;
        while (parent[i] != -1) {
            path.push_back(i);
            i = parent[i];
        }
        
        for (int p : path)
            parent[p] = i;
        return i;
    }
    
    void union_op(vector<int>& parent, int x, int y) {
        int x_set = find_parent(parent, x);
        int y_set = find_parent(parent, y);
        if (x_set != y_set)
            parent[x_set] = y_set;
    }
};