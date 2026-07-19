class Solution {
public:
    int findTargetSumWays(vector<int>& nums, int target) {
        return dfs(0, 0, nums, target);
    }
private:
    int dfs(int index, int total, vector<int>& nums, int target) {
        if (index == nums.size() && total == target) {
            return 1;
        }
        else if (index == nums.size()) {
            return 0;
        }
        return dfs(index + 1, total - nums[index], nums, target) + dfs(index + 1, total + nums[index], nums, target);
    }
};