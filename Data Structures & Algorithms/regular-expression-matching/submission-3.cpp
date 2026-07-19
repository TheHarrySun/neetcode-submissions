class Solution
{
public:
    bool isMatch(string s, string p)
    {
        return dfs(0, 0, s, p);
    }

    bool dfs(int index1, int index2, string s, string p)
    {
        if (index1 == s.length() && index2 == p.length())
        {
            return true;
        }
        else if (index1 == s.length() && ((index2 == p.length() - 1 || index2 == p.length() - 2) && p[p.length() - 1] == '*'))
        {
            return true;
        }
        else if (index1 == s.length() || index2 == p.length())
        {
            return false;
        }

        bool ans = false;
        if (s[index1] == p[index2] || p[index2] == '.')
        {
            ans = dfs(index1 + 1, index2 + 1, s, p);
        }
        else if (p[index2] == '*')
        {
            if (p[index2 - 1] == s[index1] || p[index2 - 1] == '.')
            {
                ans = ans || dfs(index1 + 1, index2, s, p) || dfs(index1, index2 + 1, s, p);
            }
            else
            {
                ans = ans || dfs(index1, index2 + 1, s, p);
            }
        }
        if (index2 < p.length() - 1 && p[index2 + 1] == '*')
        {
            ans = ans || dfs(index1, index2 + 2, s, p);
        }
        return ans;
    }
};