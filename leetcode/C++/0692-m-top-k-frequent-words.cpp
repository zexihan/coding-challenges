class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> freq;
        for (string word : words)
            freq[word]++;
        auto compare = [](pair<string, int> a, pair<string, int> b){
            if (a.second == b.second)
                return a.first < b.first;
            return a.second > b.second;
        };
        priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(compare)> pq(compare);
        for (auto const& item : freq) {
            pq.push({item.first, item.second});
            if (pq.size() > k)
                pq.pop();
        }
        vector<string> res;
        while (!pq.empty()) {
            auto p = pq.top();
            pq.pop();
            res.push_back(p.first);
        }
        reverse(res.begin(), res.end());
        return res;
    }
};