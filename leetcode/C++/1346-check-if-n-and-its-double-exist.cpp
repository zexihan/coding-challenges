class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> st;
        for (int num : arr) {
            if (st.find(num) != st.end())
                return true;
            st.insert(2 * num);
            if (num % 2 == 0)
                st.insert(num / 2);
        }
        return false;
    }
};