class Solution
{
public:
    vector<vector<bool>> memo;
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
        memo = vector<vector<bool>>(nums.size() + 1, vector<bool>(half, false));
        return dfs(nums, 0, half);
    }

    bool dfs(vector<int> &nums, int i, int half)
    {
        if (half == 0)
        {
            memo[i][half] = true;
            return true;
        }
        if (i == nums.size())
        {
            memo[i][half] = false;
            return false;
        }

        memo[i][half] = dfs(nums, i + 1, half) || dfs(nums, i + 1, half - nums[i]);
        return memo[i][half];
    }
};