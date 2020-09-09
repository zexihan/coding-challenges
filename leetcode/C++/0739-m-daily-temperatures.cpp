class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        int n = T.size();
        reverse(T.begin(), T.end());
        vector<int> span(n, 0);
        for (int i = 1; i < n; i++) {
            if (T[i] < T[i-1]) {
                span[i] = 1;
                continue;
            }
            span[i] = 1;
            while (span[i - span[i]] > 0 && T[i] >= T[i - span[i]])
                span[i] += span[i - span[i]];
            if (T[i] >= T[i - span[i]])
                span[i] = 0;
        }
        reverse(span.begin(), span.end());
        return span;
    }
};