class Solution {
public:
    int jump(vector<int>& nums) {
        int size = nums.size();
        vector<int> dp(size, 1e6);

        dp[size - 1] = 0;
        for (int i = size - 2; i >= 0; i--) {
            int end = min(i + nums[i], size - 1);
            for (int j = i + 1; j <= end; j++) {
                dp[i] = min(dp[i], 1 + dp[j]);
            }
        }
        return dp[0];
    }
};