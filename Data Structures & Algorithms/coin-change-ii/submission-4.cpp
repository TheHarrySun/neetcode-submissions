class Solution
{
public:
    int change(int amount, vector<int>& coins) {
        sort(coins.begin(), coins.end());
        vector<vector<int>> dp(coins.size(), vector<int>(amount + 1, -1));
        return dfs(coins, 0, amount, dp);
    }

    int dfs(const vector<int> coins, int i, int a, vector<vector<int>>& dp) {
        if (a == 0) {
            return 1;
        }

        if (i >= coins.size()) {
            return 0;
        }

        if (dp[i][a] != -1) {
            return dp[i][a];
        }

        int ans = 0;
        if (a >= coins[i]) {
            ans = dfs(coins, i + 1, a, dp);
            ans += dfs(coins, i, a - coins[i], dp);
        }
        dp[i][a] = ans;
        return ans;
    }
};