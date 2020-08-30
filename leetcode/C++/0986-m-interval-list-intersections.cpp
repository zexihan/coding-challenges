class Solution {
public:
    vector<vector<int>> intervalIntersection(vector<vector<int>>& A, vector<vector<int>>& B) {
        int i = 0, j = 0;
        vector<vector<int>> res;
        while (i < A.size() && j < B.size()) {
            int max_begin = max(A[i][0], B[j][0]); 
            int min_end = min(A[i][1], B[j][1]); 
            if (min_end >= max_begin) 
                res.push_back({max_begin, min_end});
            
            if (A[i][1] == min_end)
                i++;
            else
                j++;
        }
        return res;
    }
};