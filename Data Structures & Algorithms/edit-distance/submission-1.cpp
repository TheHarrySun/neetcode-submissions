class Solution
{
public:
    vector<vector<int>> dp;
    int minDistance(string word1, string word2)
    {
        dp = vector<vector<int>>(word1.length() + 1, vector<int>(word2.length() + 1, -1));
        return dfs(word1, word2, 0, 0);
    }

private:
    int dfs(string word1, string word2, int index1, int index2)
    {
        if (index1 == word1.length() && index2 == word2.length())
        {
            return 0;
        }

        if (dp[index1][index2] != -1)
        {
            return dp[index1][index2];
        }

        if (index1 == word1.length())
        {
            int ans = 1 + dfs(word1, word2, index1, index2 + 1);
            dp[index1][index2] = ans;
            return ans;
        }
        else if (index2 == word2.length())
        {
            int ans = 1 + dfs(word1, word2, index1 + 1, index2);
            dp[index1][index2] = ans;
            return ans;
        }
        if (word1[index1] == word2[index2])
        {
            int ans = dfs(word1, word2, index1 + 1, index2 + 1);
            dp[index1][index2] = ans;
            return ans;
        }
        int ans = 1 + min(dfs(word1, word2, index1 + 1, index2), min(dfs(word1, word2, index1 + 1, index2 + 1), dfs(word1, word2, index1, index2 + 1)));
        dp[index1][index2] = ans;
        return ans;
    }
};