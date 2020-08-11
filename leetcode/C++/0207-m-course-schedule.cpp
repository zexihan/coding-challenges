// Topological sort, BFS
// Time: O(N^2)
// Space: O(N)
class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_map<int, vector<int>> graph;
        unordered_map<int, int> indegrees;
        for (vector<int> c : prerequisites) {
            int course = c[0], req = c[1];
            graph[req].push_back(course);
            indegrees[course]++;
        }
        
        for (int i = 0; i < numCourses; ++i) {
            bool zeroDegree = false;
            int j = 0;
            while (j < numCourses) {
                if (indegrees[j] == 0) {
                    zeroDegree = true;
                    break;
                }
                j++;
            }
            if (!zeroDegree)
                return false;
            indegrees[j]--;
            for (int course : graph[j])
                indegrees[course]--;
        }
        return true;
    }
};