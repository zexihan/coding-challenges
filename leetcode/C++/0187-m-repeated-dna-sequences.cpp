class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        int L = 10, n = s.length();
        unordered_set<string> seen, res;
        for (int start = 0; start < n - L + 1; start++) {
            string tmp = s.substr(start, L);
            if (seen.find(tmp) != seen.end())
                res.insert(tmp);
            seen.insert(tmp);
        }
        return vector<string>(res.begin(), res.end());
    }
};