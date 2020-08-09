// Two Pointers, Greedy
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<int> last(26, 0);
        for (int i = 0; i < S.length(); i++) {
            last[S[i] - 'a'] = i;
        }
        int anchor = 0;
        int j = 0;
        vector<int> partitions;
        for (int i = 0; i < S.length(); i++) {
            j = max(j, last[S[i] - 'a']);
            if (i == j) {
                partitions.push_back(i - anchor + 1);
                anchor = i + 1;
            }
        }
        return partitions;
    }
};