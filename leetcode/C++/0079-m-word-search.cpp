// Backtracking
class Solution {
private:
    vector<vector<char>> board;
    int m, n;
    bool dfs(string word, int i, int j, int pos) {
        if (pos == word.size()) return true;
        if (i < 0 || i >= this->m || j < 0 || j >= this->n || this->board[i][j] != word[pos])
            return false;
        this->board[i][j] = '#';
        bool found = false;
        found = found || dfs(word, i+1, j, pos+1) || 
            dfs(word, i-1, j, pos+1) || 
            dfs(word, i, j+1, pos+1) || 
            dfs(word, i, j-1, pos+1);
        this->board[i][j] = word[pos];
        return found;
    }
    
public:
    bool exist(vector<vector<char>>& board, string word) {
        this->board = board;
        this->m = board.size();
        this->n = board[0].size();
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (word[0] == board[i][j] && dfs(word, i, j, 0))
                    return true;
            }
        }
        return false;
    }
};