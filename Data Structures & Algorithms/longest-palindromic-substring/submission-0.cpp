class Solution
{
public:
    string longestPalindrome(string s)
    {
        int size = s.length();

        int resLen = 0;
        int resIdx = 0;

        for (int i = 0; i < size; i++)
        {
            int l = i;
            int r = i;

            while (l >= 0 && r < size)
            {
                if (s[l] != s[r])
                {
                    break;
                }
                if (r - l + 1 > resLen)
                {
                    resLen = r - l + 1;
                    resIdx = l;
                }
                l--;
                r++;
            }
        }

        for (int i = 0; i < size - 1; i++) {
            int l = i;
            int r = i + 1;

            while (l >= 0 && r < size) {
                if (s[l] != s[r]) {
                    break;
                }
                if (r - l + 1 > resLen) {
                    resLen = r - l + 1;
                    resIdx = l;
                }
                l--;
                r++;
            }
        }

        string ans = "";
        for (int i = resIdx; i < resIdx + resLen; i++) {
            ans.push_back(s[i]);
        }
        return ans;
    }
};