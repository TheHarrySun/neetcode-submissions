class Solution
{
public:
    int findTargetSumWays(vector<int> &nums, int target)
    {
        int sum = 0;
        for (int num : nums)
        {
            sum += num;
        }

        vector<vector<int>> dp(nums.size() + 1, vector<int>(2 * sum + 1, -1));
        return dfs(0, 0, nums, target, dp, sum);
    }

private:
    int dfs(int index, int total, vector<int> &nums, int target, vector<vector<int>> &dp, int sum)
    {
        int temp = total + sum;
        if (index == nums.size() && total == target)
        {
            dp[index][temp] = 1;
            return 1;
        }
        else if (index == nums.size())
        {
            dp[index][temp] = 0;
            return 0;
        }
        if (dp[index][temp] != -1)
        {
            return dp[index][temp];
        }

        int ans = dfs(index + 1, total - nums[index], nums, target, dp, sum) + dfs(index + 1, total + nums[index], nums, target, dp, sum);
        dp[index][temp] = ans;
        return ans;
    }
};