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

// Deque: monoqueue
class Solution {
public:
    int shortestSubarray(vector<int>& A, int K) {
        int n = A.size();
        vector<int> prefix_sum(n+1, 0);
        for (int i = 0; i < n; i++)
            prefix_sum[i + 1] = prefix_sum[i] + A[i];
        
        int res = n + 1;
        deque<int> dq;
        
        for (int i = 0; i <= n; i++) {
            while (dq.size() && prefix_sum[i] <= prefix_sum[dq.back()])
                dq.pop_back();
            while (dq.size() && prefix_sum[i] - prefix_sum[dq.front()] >= K) {
                res = min(res, i - dq.front());
                dq.pop_front();
            }
            dq.push_back(i);
        }
        return res <= n ? res : -1;
    }
};