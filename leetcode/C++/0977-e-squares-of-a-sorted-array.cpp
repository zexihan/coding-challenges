// Sort
// Time: O(nlogn)
// Space: O(1)
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        auto compare = [](int a, int b) {
            return abs(a) < abs(b);
        };
        
        sort(A.begin(), A.end(), compare);
        
        for (int& num : A) 
            num *= num;
        return A;
    }
};

// Two pointers
// Time: O(n)
// Space: O(1)
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        vector<int> res(A.size());
        size_t l = 0;
        size_t r = A.size() - 1;
        size_t p = A.size() - 1;
        while (l <= r) {
            int x = A[l] * A[l];
            int y = A[r] * A[r];
            
            if (x >= y) {
                res[p] = x;
                l++;
            } else {
                res[p] = y;
                r--;
            }
            p--;
        }
        return res;
    }
};