class Solution
{
public:
    vector<vector<int>> combinationSum2(vector<int> &candidates, int target)
    {
        sort(candidates.begin(), candidates.end());
        vector<vector<int>> res;
        vector<int> curr;
        dfs(res, 0, candidates, target, curr);
        return res;
    }

    void dfs(vector<vector<int>> &res, int index, vector<int> &candidates, int target, vector<int> &curr)
    {
        if (target == 0)
        {
            res.push_back(curr);
            return;
        }
        if (target < 0 || index == candidates.size())
        {
            return;
        }
        curr.push_back(candidates[index]);
        dfs(res, index + 1, candidates, target - candidates[index], curr);
        curr.pop_back();
        if (index != candidates.size() - 1 && candidates[index + 1] == candidates[index])
        {
            int current = candidates[index];
            while (index != candidates.size() && candidates[index] == current)
            {
                index++;
            }
            dfs(res, index, candidates, target, curr);
        }
        else
        {
            dfs(res, index + 1, candidates, target, curr);
        }
    }
};