class Solution {
public:
    vector<int> findOrder(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        unordered_map<int, int> indegrees;
        vector<int> res;
        
        for (auto c : prerequisites) {
            int course = c[0], req = c[1];
            graph[req].push_back(course);
            indegrees[course]++;
        }
        
        for (int i = 0; i < numCourses; ++i) {
            int j = 0;
            bool zeroIndegree = false;
            while (j < numCourses) {
                if (indegrees[j] == 0) {
                    zeroIndegree = true;
                    res.push_back(j);
                    break;
                }
                j++;
            }
            
            if (!zeroIndegree) 
                return {};
            
            indegrees[j]--;
            for (int c : graph[j])
                indegrees[c]--;
        }
        return res;
    }
};