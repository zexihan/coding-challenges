class Solution {
    public:
        // param k : description of k
        // param n : description of n
        // return ans a integer
        int digitCounts(int k, int n) {
            int count = 0;
            if (k == 0) {
                count = 1;
            }
            for (int i = 1; i <= n; i++) {
                int number = i;
                while (number > 0) {
                    if (number % 10 == k) {
                        count += 1;
                    }
                    number /= 10;
                }
            }

            return count;
        }
};