class Solution
{
public:
    vector<vector<int>> dp;
    int longestIncreasingPath(vector<vector<int>> &matrix)
    {
        int lowest = numeric_limits<int>::min();
        int rows = matrix.size();
        int cols = matrix[0].size();
        dp = vector<vector<int>>(rows, vector<int>(cols, -1));

        int ans = 0;
        for (int i = 0; i < rows; i++)
        {
            for (int j = 0; j < cols; j++)
            {
                ans = max(ans, dfs(lowest, i, j, matrix));
            }
        }

        return ans;
    }

private:
    int dfs(int prev, int row, int col, vector<vector<int>> matrix)
    {
        int rows = matrix.size();
        int cols = matrix[0].size();
        cout << prev << " " << row << " " << col << endl;

        if (row == rows || row == -1 || col == cols || col == -1)
        {
            cout << "out of bounds" << endl;
            return 0;
        }

        int curr = matrix[row][col];

        if (prev < matrix[row][col])
        {
            if (dp[row][col] != -1)
            {
                cout << "dp " << dp[row][col] << endl;
                return dp[row][col];
            }
            int ans = 1 + max(dfs(curr, row + 1, col, matrix), max(dfs(curr, row - 1, col, matrix), max(dfs(curr, row, col + 1, matrix), dfs(curr, row, col - 1, matrix))));
            dp[row][col] = ans;
            cout << "checking ans " << dp[row][col] << endl;
            return ans;
        }
        cout << "didn't work" << endl;
        return 0;
    }
};