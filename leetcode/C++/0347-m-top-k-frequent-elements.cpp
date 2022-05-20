// Priority Queue
// Time: O(Nlogk)
// Space: O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> occurrences;
        for (auto& v : nums) {
            occurrences[v]++;
        }

        auto cmp = [](pair<int, int>& a, pair<int, int>& b) { 
            return a.second > b.second;
        };

        // pair 的第一个元素代表数组的值，第二个元素代表了该值出现的次数
        priority_queue<pair<int, int>, vector<pair<int, int>>, decltype(cmp)> pq(cmp);
        for (auto& [num, cnt] : occurrences) {
            if (pq.size() == k) {
                if (pq.top().second < cnt) {
                    pq.pop();
                    pq.emplace(num, cnt);
                }
            } else {
                pq.emplace(num, cnt);
            }
        }
        vector<int> res;
        while (!pq.empty()) {
            res.emplace_back(q.top().first);
            pq.pop();
        }
        return res;
    }
};

// Quick Sort
// Time: O(N^2)
// Space: O(N)
class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> occurrences;
        for (auto& v: nums) {
            occurrences[v]++;
        }

        vector<pair<int, int>> values;
        for (auto& kv: occurrences) {
            values.push_back(kv);
        }
        vector<int> res;
        qsort(values, 0, values.size() - 1, res, k);
        return res;
    }

    void qsort(vector<pair<int, int>>& v, int start, int end, vector<int>& res, int k) {
        int picked = rand() % (end - start + 1) + start;
        swap(v[picked], v[start]);

        int pivot = v[start].second;
        int index = start;
        for (int i = start + 1; i <= end; i++) {
            if (v[i].second >= pivot) {
                swap(v[index + 1], v[i]);
                index++;
            }
        }
        swap(v[start], v[index]);

        if (k <= index - start) {
            qsort(v, start, index - 1, res, k);
        } else {
            for (int i = start; i <= index; i++) {
                ret.push_back(v[i].first);
            }
            if (k > index - start + 1) {
                qsort(v, index + 1, end, res, k - (index - start + 1));
            }
        }
    }
};
