// Greedy
class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();
        if (n == 0) return 0;
        auto compare = [](vector<int>& a, vector<int>& b){
            return a[1] < b[1];
        };
        sort(intervals.begin(), intervals.end(), compare);
        int res = 0;
        int cur = 0, next = 1;
        while (next < n) {
            while (next < n && intervals[next][0] < intervals[cur][1]) {
                res++;
                next++;
            }
            cur = next;
            next++;
        }
        return res;
    }
};