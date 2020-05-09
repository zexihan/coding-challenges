/**
 * Definition of Interval:
 * classs Interval {
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
    public:
        int minMeetingRooms(vector<Interval> &intervals) {
            map<int, int> m;
            for (auto a : intervals) {
                ++m[a.start];
                --m[a.end];
            }
            int rooms = 0, res = 0;
            for (auto it : m) {
                res = max(res, rooms += it.second);
            }
            return res;
        }
};