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
        if (size == 2)
        {
            return max(nums[0], nums[1]);
        }
        int money[nums.size()];
        money[0] = nums[0];
        money[1] = nums[1];
        money[2] = nums[0] + nums[2];
        for (int i = 3; i < size; i++)
        {
            money[i] = nums[i] + max(money[i - 2], money[i - 3]);
        }

        return max(money[size - 1], money[size - 2]);
    }
};