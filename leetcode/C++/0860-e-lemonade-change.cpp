// Greedy, Simulation
class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int five = 0, ten = 0;
        for (int bill : bills) {
            if (bill == 10) {
                five--;
                ten++;
            } else if (bill == 20) {
                if (ten > 0) {
                    ten--;
                    five--;
                } else 
                    five -= 3;
            } else 
                five++;
            if (five < 0 || ten < 0)
                return false;
        }
        return true;
    }
};