// Heap
// let X = min(K, N)
// Time: O(X + Klog(X))
// Space: O(X)
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int N = matrix.size();
        
        auto compare = [](tuple<int, int, int> a, tuple<int, int, int> b) { 
            return get<0>(a) > get<0>(b); 
        };
        priority_queue<tuple<int, int, int>, vector<tuple<int, int, int>>, decltype(compare)> minHeap(compare);
        
        for (int r = 0; r < min(N, k); r++) {
            minHeap.push(make_tuple(matrix[r][0], r, 0));
        }
        
        auto element = minHeap.top();
        
        while (k-- > 0) {
            element = minHeap.top();
            minHeap.pop();
            int r = get<1>(element), c = get<2>(element);
            
            if (c < N - 1) {
                minHeap.push(make_tuple(matrix[r][c + 1], r, c + 1));
            }
        }
        return get<0>(element);
    }
};

// Binary search
// Time: O(N x log(Max - Min))
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        // l is the smallest and r is the largest
        int l = matrix[0][0], r = matrix[n-1][n-1], mid;
        while (l < r){
            mid = l + r >> 1;
            int cnt = 0, i = n - 1;
            for (int j = 0; j < n; j++){
                while (i >= 0 && matrix[i][j] > mid)
                    i--;
                cnt += i + 1;
            }
            if (cnt < k)
                l = mid + 1; // search higher
            else
                r = mid; // search lower
        }
        return l;
    }
};