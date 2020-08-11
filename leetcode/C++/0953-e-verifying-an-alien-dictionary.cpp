// Hash table
// Time: O(C), where C is the total content of words
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {
        unordered_map<char, int> order_index;
        for (int i = 0; i < order.length(); i++) {
            order_index[order[i]] = i;
        }
        
        for (int i = 0; i < words.size() - 1; i++) {
            string word1 = words[i];
            string word2 = words[i + 1];
            
            int k = 0;
            int check_length = min(word1.length(), word2.length());
            for (; k < check_length; k++) {
                if (word1[k] != word2[k]) {
                    if (order_index[word1[k]] > order_index[word2[k]])
                        return false;
                    break;
                }
            }
            // ("apple", "app")
            if (k == check_length && word1.length() > word2.length())
                return false;
        }
        return true;
    }
};