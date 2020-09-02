class Solution {
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;
        for (int i = 0; i < input.length(); i++) {
            if (input[i] < '0' || input[i] > '9') {
                vector<int> left = diffWaysToCompute(input.substr(0, i));
                vector<int> right = diffWaysToCompute(input.substr(i+1));
                for (int l : left) {
                    for (int r : right) {
                        if (input[i] == '+') res.push_back(l + r);
                        else if (input[i] == '-') res.push_back(l - r);
                        else res.push_back(l * r);
                    }
                }
            }
        }
        if (res.empty())
            res.push_back(stoi(input));
        return res;
    }
};