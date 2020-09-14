class Solution {
private:
    int find_parent(int p, vector<int>& parent) {
        while (p != parent[p]) {
            parent[p] = parent[parent[p]];
            p = parent[p];
        }
        return p;
    }
    
    void union_op(int a, int b, int& islands, vector<int>& parent) {
        int parent_a = find_parent(a, parent);
        int parent_b = find_parent(b, parent);
        if (parent_a != parent_b) {
            parent[parent_a] = parent_b;
            islands--;
        }
    }
    
public:
    vector<int> numIslands2(int m, int n, vector<vector<int>>& positions) {
        vector<int> parent(m * n, -1);
        vector<vector<int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};
        vector<int> res;
        int islands = 0;
        for (int i = 0; i < positions.size(); i++) {
            int x = positions[i][0], y = positions[i][1];
            int idx_p = x * n + y;
            if (parent[idx_p] != -1) {
                res.push_back(islands);
                continue;
            }
            parent[idx_p] = idx_p;
            islands++;
            for (vector<int> d : directions) {
                int nx = x + d[0], ny = y + d[1];
                int idx_nei = nx * n + ny;
                if (0 <= nx && nx < m && 0 <= ny && ny < n && parent[idx_nei] != -1) {
                    union_op(idx_p, idx_nei, islands, parent);
                }
            }
            res.push_back(islands);
        }
        return res;
    }
};