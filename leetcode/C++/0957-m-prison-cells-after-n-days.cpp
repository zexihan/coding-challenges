class Solution {
public:
    vector<int> prisonAfterNDays(vector<int>& cells, int N) {
        vector<int> prev = cells, cur(cells.size(), 0), first_state;
        for (int cycle = 0; N-- > 0; cycle++) {
            for (int p = 1; p < cells.size() - 1; p++)
                cur[p] = prev[p-1] == prev[p+1];
            if (cycle == 0) 
                first_state = cur;
            else if (cur == first_state)
                N %= cycle;
            prev = cur;
        }
        return prev;
    }
};