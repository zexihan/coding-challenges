class Solution {
public:
    vector<int> exclusiveTime(int n, vector<string>& logs) {
        vector<int> res(n, 0);
        stack<int> stk;
        int prev;
        for (int i = 0; i < logs.size(); i++) {
            int pos1 = logs[i].find(':');
            int pos2 = logs[i].find(':', pos1 + 1);
            int id = stoi(logs[i].substr(0, pos1));
            string type = logs[i].substr(pos1 + 1, pos2 - pos1 - 1);
            int timestamp = stoi(logs[i].substr(pos2 + 1, logs[i].length() - pos2));
            if (i == 0) {
                prev = timestamp;
                stk.push(id);
                continue;
            }
            if (type == "start") {
                if (!stk.empty())
                    res[stk.top()] += timestamp - prev;
                stk.push(id);
                prev = timestamp;
            } else {
                res[stk.top()] += timestamp - prev + 1;
                stk.pop();
                prev = timestamp + 1;
            }
        }
        return res;
    }
};