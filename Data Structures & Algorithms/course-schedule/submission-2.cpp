class Solution
{
    unordered_map<int, vector<int>> prereqs;
    unordered_set<int> visited;

public:
    bool canFinish(int numCourses, vector<vector<int>> &prerequisites)
    {
        for (int i = 0; i < numCourses; i++)
        {
            prereqs[i] = {};
        }
        for (auto prereq : prerequisites)
        {
            prereqs[prereq[0]].push_back(prereq[1]);
        }
        for (int i = 0; i < numCourses; i++)
        {
            if (!dfs(i))
            {
                return false;
            }
        }
        return true;
    }

    bool dfs(int course)
    {
        if (prereqs[course].empty())
        {
            return true;
        }
        if (visited.count(course))
        {
            return false;
        }
        visited.insert(course);
        for (int prereq : prereqs[course])
        {
            if (!dfs(prereq))
            {
                return false;
            }
        }
        visited.erase(course);
        prereqs[course].clear();
        return true;
    }
};