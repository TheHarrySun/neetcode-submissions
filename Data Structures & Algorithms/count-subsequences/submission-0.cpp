class Solution
{
public:
    vector<vector<int>> dp;
    int numDistinct(string s, string t)
    {
        dp = vector<vector<int>>(s.length(), vector<int>(t.length(), -1));
        return dfs(0, 0, s, t);
    }

    int dfs(int s_index, int t_index, string s, string t)
    {
        if (t_index == t.length())
        {
            return 1;
        }
        else if (s_index == s.length())
        {
            return 0;
        }

        if (dp[s_index][t_index] != -1)
        {
            return dp[s_index][t_index];
        }

        int ans;
        if (s[s_index] == t[t_index])
        {
            ans = dfs(s_index + 1, t_index + 1, s, t) + dfs(s_index + 1, t_index, s, t);
        }
        else
        {
            ans = dfs(s_index + 1, t_index, s, t);
        }
        dp[s_index][t_index] = ans;
        return ans;
    }
};