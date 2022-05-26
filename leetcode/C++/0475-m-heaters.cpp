class Solution {
public:
    int findRadius(vector<int>& houses, vector<int>& heaters) {
        sort(houses.begin(), houses.end());
        sort(heaters.begin(), heaters.end());
        int res = 0;
        for (int i = 0, j = 0; i < houses.size(); i++) {
            int cur_dist = abs(houses[i] - heaters[j]);
            while (j < heaters.size() - 1 && abs(houses[i] - heaters[j]) >= abs(houses[i] - heaters[j + 1])) {
                j++;
                cur_dist = min(cur_dist, abs(houses[i] - heaters[j]));
            }
            res = max(res, cur_dist);
        }
        return res;
    }
};
