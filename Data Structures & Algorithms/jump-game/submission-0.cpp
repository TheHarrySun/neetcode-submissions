class Solution
{
public:
    bool canJump(vector<int> &nums)
    {
        int size = nums.size();
        if (size == 1)
        {
            return true;
        }
        vector<bool> dp(size, false);
        dp[size - 1] = true;
        for (int i = size - 2; i >= 0; i--)
        {
            for (int j = i; j <= i + nums[i]; j++)
            {
                if (dp[j] == true || j >= size)
                {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};