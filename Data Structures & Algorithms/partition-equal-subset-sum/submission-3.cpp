class Solution
{
public:
    vector<vector<int>> memo;
    bool canPartition(vector<int> &nums)
    {
        int sum = 0;
        for (int num : nums)
        {
            sum += num;
        }
        if (sum % 2 == 1)
        {
            return false;
        }
        int half = sum / 2;
        memo.resize(nums.size(), vector<int>(half + 1, -1));
        return dfs(nums, 0, half);
    }

    bool dfs(vector<int> &nums, int i, int half)
    {
        if (i == nums.size())
        {
            return half == 0;
        }
        if (half < 0) {
            return false;
        }
        if (memo[i][half] != -1)
        {
            return memo[i][half];
        }
        memo[i][half] = dfs(nums, i + 1, half) || dfs(nums, i + 1, half - nums[i]);
        return memo[i][half];
    }
};