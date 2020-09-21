// Greedy
class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> frequencies(26, 0);
        for (char c : tasks)
            frequencies[c - 'A']++;
        sort(frequencies.begin(), frequencies.end());
        int f_max = frequencies[25];
        int idle_time = (f_max - 1) * n;
        for (int i = frequencies.size() - 2; i > -1; i --) {
            idle_time -= min(f_max - 1, frequencies[i]);
        }
        idle_time = max(0, idle_time);
        return idle_time + tasks.size();
    }
};