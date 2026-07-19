class Solution
{
public:
    int maxCoins(vector<int> &nums)
    {
        vector<vector<int>> dp(nums.size() + 2, vector<int>(nums.size() + 2, -1));
        vector<int> new_nums = vector<int>(nums.size() + 2, 1);
        for (int i = 1; i <= nums.size(); i++)
        {
            new_nums[i] = nums[i - 1];
        }
        return dfs(1, nums.size(), new_nums, dp);
    }

    int dfs(int first, int last, vector<int> &nums, vector<vector<int>> &dp)
    {
        if (dp[first][last] != -1)
        {
            return dp[first][last];
        }
        int ans = 0;
        for (int i = first; i <= last; i++)
        {
            int temp = nums[i] * nums[first - 1] * nums[last + 1];
            if (i == first)
            {
                temp += dfs(i + 1, last, nums, dp);
            }
            else if (i == last)
            {
                temp += dfs(first, i - 1, nums, dp);
            }
            else
            {
                temp += dfs(first, i - 1, nums, dp) + dfs(i + 1, last, nums, dp);
            }
            ans = max(ans, temp);
        }
        dp[first][last] = ans;
        return ans;
    }
};