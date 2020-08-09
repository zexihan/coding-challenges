/*  
Math - Integer Factorisation
N=(x+1)+...+(x+k)
N=xk+(1+2+...+k)
N=xk+k(k+1)/2
2N=k(2x+k+1)

x=N/k-(k+1)/2
Two constraints:
1) x >= 0
2) x is an integer

k <= sqrt(2N+1/4)-1/2

Time: O(sqrt(N))
*/
class Solution {
public:
    int consecutiveNumbersSum(int N) {
        int count = 0;
        int upper_limit = sqrt(2 * N + 0.25) - 0.5;
        for (int k = 1; k <= upper_limit; ++k) {
            if ((N - k * (k + 1) / 2) % k == 0)
                count++;
        }
        return count;
    }
};

