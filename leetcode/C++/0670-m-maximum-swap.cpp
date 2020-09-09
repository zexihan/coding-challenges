class Solution {
public:
    int maximumSwap(int num) {
        string A = to_string(num);
        vector<int> last(10, 0);
        for (int i = 0; i < A.length(); i++) {
            last[A[i] - '0'] = i;
        }
        for (int i = 0; i < A.length(); i++) {
            for (int d = 9; d > A[i] - '0'; d--) {
                if (last[d] > i) {
                    swap(A[i], A[last[d]]);
                    return stoi(A);
                }
            }
        }
        return num;
    }
};