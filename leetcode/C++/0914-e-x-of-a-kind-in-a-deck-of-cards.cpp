// Math
// Time: O(Nlog^2(N))
Space: O(N)
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        unordered_map<int, int> counter;
        for (int n : deck)
            counter[n]++;
        
        int g = -1;
        auto it = counter.begin();
        while(it != counter.end()) {
            if (it->second > 0) 
                g = it->second;
            else
                g = gcd(g, it->second);
            it++;
        }
        return g >= 2;
    }
    
    int gcd(int x, int y) {
        return x == 0 ? y : gcd(y%x, x);
    }
};