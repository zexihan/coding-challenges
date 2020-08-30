class Solution {
public:
    int numJewelsInStones(string J, string S) {
        unordered_set<char> st;
        for (char j : J)
            st.insert(j);
        int res = 0;
        for (char s : S)
            if (st.find(s) != st.end())
                res++;
        return res;
    }
};