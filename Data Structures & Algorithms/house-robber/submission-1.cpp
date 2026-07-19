class Solution
{
public:
    int rob(vector<int> &nums)
    {
        int size = nums.size();
        if (size == 1)
        {
            return nums[0];
        }
        int money[nums.size()];
        money[0] = nums[0];
        money[1] = max(nums[1], nums[0]);
        for (int i = 2; i < size; i++)
        {
            money[i] = max(money[i - 2] + nums[i], money[i - 1]);
        }

        return money[size - 1];
    }
};