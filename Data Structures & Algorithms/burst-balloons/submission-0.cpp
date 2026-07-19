class Solution
{
public:
    int maxCoins(vector<int> &nums)
    {
        vector<int> new_nums = vector<int>(nums.size() + 2, 1);
        for (int i = 1; i <= nums.size(); i++)
        {
            new_nums[i] = nums[i - 1];
        }
        return dfs(1, nums.size(), new_nums);
    }

    int dfs(int first, int last, vector<int> &nums)
    {
        int ans = 0;
        for (int i = first; i <= last; i++)
        {
            int temp = nums[i] * nums[first - 1] * nums[last + 1];
            if (i == first)
            {
                temp += dfs(i + 1, last, nums);
            }
            else if (i == last)
            {
                temp += dfs(first, i - 1, nums);
            }
            else
            {
                temp += dfs(first, i - 1, nums) + dfs(i + 1, last, nums);
            }
            ans = max(ans, temp);
        }
        return ans;
    }
};