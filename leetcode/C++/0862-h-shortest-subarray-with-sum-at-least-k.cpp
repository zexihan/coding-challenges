// Brute force, TLE
class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        int res = INT_MAX;
        int N = A.size();
        for (int i = 0; i < N; i++) {
            int curSum = 0;
            for (int j = i; j < N; j++) {
                curSum += A[j];
                if (curSum >= K)
                    res = min(res, j - i + 1);
            }
        }
        
        return res == INT_MAX ? -1 : res;
    }
};

// Priority queue
class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        int res = INT_MAX;
        int sum = 0;
        for (int i = 0; i < A.size(); i++) {
            sum += A[i];
            if (sum >= K)
                res = min(res, i + 1);
            while (!pq.empty() && sum - pq.top().first >= K) {
                auto &p = pq.top();
                res = min(res, i - p.second);
                pq.pop();
            }
            pq.push({sum, i});
        }
        return res == INT_MAX ? -1 : res;
    }
};

// Deque
class Solution {
public:
    int shortestSubarray(vector<int> A, int K) {
        int N = A.size(), res = N + 1;
        deque<int> d;
        for (int i = 0; i < N; i++) {
            if (i > 0)
                A[i] += A[i - 1];
            if (A[i] >= K)
                res = min(res, i + 1);
            while (d.size() && A[i] - A[d.front()] >= K) {
                res = min(res, i - d.front());
                d.pop_front();
            }
            while (d.size() && A[i] <= A[d.back()])
                d.pop_back();
            d.push_back(i);
        }
        return res <= N ? res : -1;
    }
};