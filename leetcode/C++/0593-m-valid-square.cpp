class Solution {
public:
    bool validSquare(vector<int>& p1, vector<int>& p2, vector<int>& p3, vector<int>& p4) {
        vector<double> edge_lens = {
            pow(p2[0] - p1[0], 2) + pow(p2[1] - p1[1], 2),
            pow(p3[0] - p1[0], 2) + pow(p3[1] - p1[1], 2),
            pow(p4[0] - p1[0], 2) + pow(p4[1] - p1[1], 2),
            pow(p3[0] - p2[0], 2) + pow(p3[1] - p2[1], 2),
            pow(p4[0] - p2[0], 2) + pow(p4[1] - p2[1], 2),
            pow(p4[0] - p3[0], 2) + pow(p4[1] - p3[1], 2),
        };
        sort(edge_lens.begin(), edge_lens.end());
        if (edge_lens[0] != edge_lens[1] || 
            edge_lens[0] != edge_lens[2] ||
            edge_lens[0] != edge_lens[3] ||
            edge_lens[4] != edge_lens[5] ||
            edge_lens[0] == edge_lens[4])
            return false;
        if (edge_lens[0] + edge_lens[1] != edge_lens[4])
            return false;
        return true;
    }
};