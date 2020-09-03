// BFS
// Time: O(M x N)
// Space: O(min(M, N))
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        int num_islands = 0;
        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1') {
                    ++num_islands;
                    grid[r][c] = '0'; // mark as visited
                    queue<pair<int, int>> neighbors;
                    neighbors.push({r, c});
                    while (!neighbors.empty()) {
                        auto rc = neighbors.front();
                        neighbors.pop();
                        int row = rc.first, col = rc.second;
                        for (auto d : directions) {
                            int row_cur = row + d.first, col_cur = col + d.second;
                            if (row_cur >= 0 && row_cur < nr &&
                                col_cur >= 0 && col_cur < nc &&
                                grid[row_cur][col_cur] == '1') {
                                neighbors.push({row_cur, col_cur}); 
                                grid[row_cur][col_cur] = '0';
                            }
                        }
                    }
                }
            }
        }
        return num_islands;
    }
};

// DFS
// Time: O(M x N)
// Space: O(M x N)
class Solution {
private:
    void dfs(int i, int j, vector<vector<char>>& grid) {
        if (i < 0 || j < 0 || i > grid.size() - 1 || j > grid[0].size() - 1 || grid[i][j] == '0')
            return;
        grid[i][j] = '0';
        dfs(i + 1, j, grid);
        dfs(i - 1, j, grid);
        dfs(i, j + 1, grid);
        dfs(i, j - 1, grid);
    }
    
public:
    int numIslands(vector<vector<char>>& grid) {
        int res = 0;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                if (grid[i][j] == '1') {
                    res += 1;
                    dfs(i, j, grid);
                }
            }
        }
        return res;
    }
};

// Union Find
// Time: O(M x N)
// Space: O(M x N)
typedef pair<int, int> pair_rc;
struct hash_pair { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const
    { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
}; 
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();
        
        int num_islands = 0;
        map<pair_rc, pair_rc> parent;
        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1')
                    parent[make_pair(r, c)] = make_pair(r, c);
            }
        }
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1') {
                    num_islands++;
                    for (auto d : directions) {
                        int row = r + d.first, col = c + d.second;
                        if (row < 0 || row >= nr || col < 0 || col >= nc)
                            continue;
                        if (grid[row][col] == '1')
                            union_op(make_pair(r, c), make_pair(row, col), num_islands, parent);
                    }
                }
            }
        }
        return num_islands;
    }

    void union_op(pair_rc point_a, pair_rc point_b, 
                  int& num_islands, map<pair_rc, pair_rc>& parent) {
        auto root_a = find_op(point_a, parent);
        auto root_b = find_op(point_b, parent);
        if (root_a != root_b) {
            parent[root_a] = root_b;
            num_islands--;
        }
    }

    pair_rc find_op(pair_rc point, map<pair_rc, pair_rc>& parent) {
        vector<pair_rc> path;
        while (point != parent[point]) {
            path.push_back(point);
            point = parent[point];
        }

        for (auto p : path)
            parent[p] = point;
        
        return point;
    }
};


// Use unordered_map
typedef pair<int, int> pair_rc;
struct hash_pair { 
    template <class T1, class T2> 
    size_t operator()(const pair<T1, T2>& p) const
    { 
        auto hash1 = hash<T1>{}(p.first); 
        auto hash2 = hash<T2>{}(p.second); 
        return hash1 ^ hash2; 
    } 
}; 
class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int nr = grid.size();
        if (!nr) return 0;
        int nc = grid[0].size();
        
        int num_islands = 0;
        unordered_map<pair_rc, pair_rc, hash_pair> parent;
        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1')
                    parent[make_pair(r, c)] = make_pair(r, c);
            }
        }
        
        vector<pair<int, int>> directions = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

        for (int r = 0; r < nr; ++r) {
            for (int c = 0; c < nc; ++c) {
                if (grid[r][c] == '1') {
                    num_islands++;
                    for (auto d : directions) {
                        int row = r + d.first, col = c + d.second;
                        if (row < 0 || row >= nr || col < 0 || col >= nc)
                            continue;
                        if (grid[row][col] == '1')
                            union_op(make_pair(r, c), make_pair(row, col), num_islands, parent);
                    }
                }
            }
        }
        return num_islands;
    }

    void union_op(pair_rc point_a, pair_rc point_b, 
                  int& num_islands, unordered_map<pair_rc, pair_rc, hash_pair>& parent) {
        auto root_a = find_op(point_a, parent);
        auto root_b = find_op(point_b, parent);
        if (root_a != root_b) {
            parent[root_a] = root_b;
            num_islands--;
        }
    }

    pair_rc find_op(pair_rc point, unordered_map<pair_rc, pair_rc, hash_pair>& parent) {
        vector<pair_rc> path;
        while (point != parent[point]) {
            path.push_back(point);
            point = parent[point];
        }

        for (auto p : path)
            parent[p] = point;
        
        return point;
    }
};