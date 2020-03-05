// two pointers + map
class Solution
{
public:
    string minWindow(string &source, string &target)
    {
        unordered_map<char, int> mp;
        for (char t : target)
            mp[t]++;
        int count = mp.size();
        int j = 0;
        int ans = INT_MAX;
        string res;
        for (int i = 0; i < source.size(); i++)
        {
            while (count != 0 && j < source.size())
            {
                mp[source[j]]--;
                if (mp[source[j]] == 0)
                    count--;
                j++;
                if (count == 0)
                    break;
            }
            if (count == 0 && j - i < ans)
            {
                ans = j - i;
                res = source.substr(i, j - i);
            }
            if (mp[source[i]] == 0)
                count++;
            mp[source[i]]++;
        }
        return res;
    }
};