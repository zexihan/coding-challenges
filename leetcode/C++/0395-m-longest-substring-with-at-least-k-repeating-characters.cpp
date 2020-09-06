class Solution {
public:
    int longestSubstring(string s, int k) {
        int n = s.length();
        vector<int> count(26, 0);
        for (char c : s) 
            count[c - 'a']++;
        
        int mid = 0;
        while (mid < n && count[s[mid] - 'a'] >= k) 
            mid++;
        if (mid == n) 
            return n;
        
        int left = longestSubstring(s.substr(0, mid), k);
        
        while (mid < n && count[s[mid] - 'a'] < k) 
            mid++;
        
        int right = longestSubstring(s.substr(mid), k);
        
        return max(left, right);
    }
};