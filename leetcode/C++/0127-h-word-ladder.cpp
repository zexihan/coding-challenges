// BFS
// Time: O(M^2xN) where M is the length of each word and N is the total number of words in the input word list.
// Space: O(M^2xN)
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        string alpha = "abcdefghijklmnopqrstuvwxyz";
        unordered_set<string> wordSet(wordList.begin(), wordList.end());
        queue<pair<string, int>> q;
        q.push({beginWord, 1});
        while (!q.empty()) {
            string w = q.front().first;
            int lens = q.front().second;
            q.pop();
            if (w == endWord) return lens;
            for (int i = 0; i < w.length(); i++) {
                for (char c : alpha) {
                    string nw = w.substr(0, i) + c + w.substr(i + 1);
                    if (wordSet.find(nw) != wordSet.end() && nw != w) {
                        q.push({nw, lens + 1});
                        wordSet.erase(nw);
                    }
                }  
            }
        }
        return 0;
    }
};