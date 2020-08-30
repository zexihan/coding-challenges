// DFS
class Solution {
private:
    unordered_map<int, vector<int>> graph;
    unordered_map<int, int> color;
    
public:
    bool possibleBipartition(int N, vector<vector<int>>& dislikes) {
        
        for (auto edge : dislikes) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        for (int node = 1; node <= N; node++)
            if (color.find(node) == color.end() && !dfs(node, 0))
                return false;
        return true;
    }
    
    bool dfs(int node, int c) {
        if (color.find(node) != color.end())
            return color[node] == c;
        color[node] = c;
        
        for (int nei : graph[node])
            if (!dfs(nei, c ^ 1))
                return false;
        return true;
    }
};