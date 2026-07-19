class Solution
{
public:
    unordered_set<int> visited;
    unordered_set<int> path;
    unordered_map<int, vector<int>> edgeMap;

    bool validTree(int n, vector<vector<int>> &edges)
    {
        for (auto edge : edges)
        {
            edgeMap[edge[0]].push_back(edge[1]);
            edgeMap[edge[1]].push_back(edge[0]);
        }

        if (!dfs(0, -1))
        {
            return false;
        }
        for (int i = 0; i < n; i++)
        {
            if (!visited.count(i))
            {
                return false;
            }
        }
        return true;
    }

    bool dfs(int node, int parent)
    {
        if (path.count(node))
        {
            return false;
        }

        path.insert(node);
        for (int next : edgeMap[node])
        {
            if (next == parent)
            {
                continue;
            }
            if (!dfs(next, node))
            {
                return false;
            }
        }
        path.erase(node);
        if (!visited.count(node))
        {
            visited.insert(node);
        }
        return true;
    }
};