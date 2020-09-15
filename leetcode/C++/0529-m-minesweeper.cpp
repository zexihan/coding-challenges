class Solution {
public:
    vector<vector<char>> updateBoard(vector<vector<char>>& a, vector<int>& b) {
        queue<pair<int,int>> q;
        int n = a.size(), m = a[0].size();
        vector<int> dx = { -1, -1, -1, 0, 0, 1, 1, 1 };
        vector<int> dy = { -1, 0, 1, -1, 1, -1, 0, 1 };
        if (a[b[0]][b[1]] == 'M')      
            a[b[0]][b[1]] = 'X'; 
        else if (a[b[0]][b[1]] == 'E') 
            q.push({b[0],b[1]});
        while (!q.empty()) {
            int x = q.front().first, y = q.front().second, cnt = 0; q.pop();
            vector<pair<int,int>> aux;
            for (int i = 0; i < 8; i++) {
                int u = x+dx[i], v = y+dy[i];
                if (u < 0 || v < 0 || u >= n || v >= m)     
                    continue;
                else if (a[u][v] == 'M' || a[u][v] == 'X')  
                    cnt++;
                else if (a[u][v] == 'E')                    
                    aux.push_back({u,v});
            }
            
            a[x][y] = '0' + cnt;
            if (a[x][y] > '0') 
                continue;
            else               
                a[x][y] = 'B';
            for (auto s : aux) {
                a[s.first][s.second] = 'B';     // flag
                q.push(s);
            }
        }
        return a;
    }
};