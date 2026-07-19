class Solution
{
public:
    string longestPalindrome(string s)
    {
        int size = s.length();
        vector<vector<bool>> palindrome(size, vector<bool>(size, false));

        int resLen = 0;
        int resIdx = 0;

        for (int i = size - 1; i >= 0; i--)
        {
            for (int j = i; j < size; j++)
            {
                if (s[i] == s[j] && (j - i <= 2 || palindrome[i + 1][j - 1]))
                {
                    palindrome[i][j] = true;
                    if (j - i + 1 > resLen)
                    {
                        resLen = j - i + 1;
                        resIdx = i;
                    }
                }
            }
        }

        return s.substr(resIdx, resLen);
    }
};