class Solution
{
public:
    int maxSubArray(vector<int> &nums)
    {
        vector<vector<int>> dp(nums.size() + 1, vector<int>(2, INT_MIN));
        return dfs(0, nums, false, dp);
    }

private:
    int dfs(int index, vector<int> nums, bool flag, vector<vector<int>>& dp)
    {
        if (index == nums.size())
        {
            return flag ? 0 : INT_MIN;
        }
        int i = flag ? 1: 0;
        if (dp[index][i] != INT_MIN) {
            return dp[index][i];
        }
        if (flag) {
            dp[index][i] = max(0, nums[index] + dfs(index + 1, nums, flag, dp));
        }
        else {
            dp[index][i] = max(dfs(index + 1, nums, flag, dp), nums[index] + dfs(index + 1, nums, true, dp));
        }
        return dp[index][i];
    }
};
