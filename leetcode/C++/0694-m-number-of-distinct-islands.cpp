// DFS
class Solution {
private:
    void dfs(int i, int j, string& path, vector<vector<int>>& grid, char d) {
        if (i < 0 || j < 0 || i > grid.size() - 1 || j > grid[0].size() - 1 || grid[i][j] == 0)
            return;
        path.push_back(d);
        grid[i][j] = 0;
        dfs(i-1, j, path, grid, 'u');
        dfs(i+1, j, path, grid, 'd');
        dfs(i, j-1, path, grid, 'l');
        dfs(i, j+1, path, grid, 'r');
        path.push_back('b');
    }
    
public:
    int numDistinctIslands(vector<vector<int>>& grid) {
        unordered_set<string> st;
        for (int i = 0; i < grid.size(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                string path = "";
                if (grid[i][j] == 1) 
                    dfs(i, j, path, grid, 'x');
                if (!path.empty())  
                    st.insert(path);
            }
        }
        return st.size();
    }
};