// DFS
class Solution {
private:
    bool hasCycle(unordered_map<int, vector<int>>& graph, int cur, int pre, vector<bool>& visited) {
        if (visited[cur]) return true;
        visited[cur] = true;
        for (int next : graph[cur]) {
            if (next != pre && hasCycle(graph, next, cur, visited))
                return true;
        }
        return false;
    }
        
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        unordered_map<int, vector<int>> graph;
        vector<bool> visited(n, false);
        for (int i = 0; i < edges.size(); i++) {
            graph[edges[i][0]].push_back(edges[i][1]);
            graph[edges[i][1]].push_back(edges[i][0]);
        }
        
        if (hasCycle(graph, 0, -1, visited))
            return false;
        
        for (bool v : visited)
            if (!v) return false;
        
        return true;
    }
};

// Union Find
class Solution {
public:
    bool validTree(int n, vector<vector<int>>& edges) {
        if (edges.size() != n - 1)
            return false;
        
        vector<int> parent(n, -1);
        int x, y;
        for (int i = 0; i < n - 1; i++) {
            x = find_parent(parent, edges[i][0]);
            y = find_parent(parent, edges[i][1]);
            if (x == y)
                return false;
            else
                union_op(parent, x, y);
        }
        
        return true;
    }
    
    int find_parent(vector<int>& parent, int i) {
        if (parent[i] == -1)
            return i;
        return find_parent(parent, parent[i]);
    }
    
    void union_op(vector<int>& parent, int x, int y) {
        int x_set = find_parent(parent, x);
        int y_set = find_parent(parent, y);
        
        if (x_set != y_set)
            parent[x_set] = y_set;
    }
};