class Solution
{
public:
    vector<vector<int>> kClosest(vector<vector<int>> &points, int k)
    {
        unordered_map<double, vector<vector<int>>> mapping;
        priority_queue<double, vector<double>, greater<double>> minheap;
        for (vector<int> point : points)
        {
            double dist = pow(point[0], 2) + pow(point[1], 2);
            mapping[dist].push_back(point);
            minheap.push(dist);
        }
        vector<vector<int>> ans(k);
        for (int i = 0; i < k; i++)
        {
            int closest = minheap.top();
            minheap.pop();
            ans[i] = mapping[closest][0];
            mapping[closest].erase(mapping[closest].begin());
        }
        return ans;
    }
};