class Solution {
public:
    string removeKdigits(string num, int k) {
        deque<char> dq;
        for (char digit : num) {
            while (k > 0 && !dq.empty() && dq.back() > digit) {
                dq.pop_back();
                k--;
            }
            dq.push_back(digit);
        }
        for (int i = 0; i < k; i++)
            dq.pop_back();
        string res = "";
        bool leadingZero = true;
        while (!dq.empty()) {
            if (leadingZero && dq.front() == '0') {
                dq.pop_front();
                continue;
            }
            leadingZero = false;
            res += dq.front();
            dq.pop_front();
        }
        if (res.length() == 0) return "0";
        return res;
    }
};