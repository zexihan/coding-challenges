// Hash table, String
// Time: O(N)
// Space: O(N)
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        vector<string> res;
        unordered_map<string, int> visitCount;
        
        for (string cpd : cpdomains) {
            int vc = stoi(cpd.substr(0, cpd.find(' ')));
            string d = cpd.substr(cpd.find(' ') + 1, cpd.length());
            
            visitCount[d] += vc;
                
            int dotpos = d.find('.');
            while (dotpos != string::npos) {
                string subd = d.substr(dotpos + 1, d.length());
                visitCount[subd] += vc;
                dotpos = d.find('.', dotpos + 1);
            }
        }
        
        auto it = visitCount.cbegin();
        while (it != visitCount.cend()) {
            res.push_back(to_string(it->second) + ' ' + it->first);
            it++;
        }
        return res;
    }
};