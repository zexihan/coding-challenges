class Solution {
public:
    bool isHappy(int n) {
        int slow = n, fast = n;
        while (slow != 1) {
            slow = transform(slow);
            fast = transform(fast);
            fast = transform(fast);
            if (slow == fast)
                break;
        }
        if (slow == 1) return true;
        return false;
    }
    
    int transform(int n) {
        int res = 0;
        while (n) {
            res += (n % 10) * (n % 10);
            n /= 10;
        }
        return res;
    }
};