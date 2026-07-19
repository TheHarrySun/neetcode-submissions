class Solution
{
public:
    int numDecodings(string s)
    {
        int length = s.length();

        vector<int> num(length);
        
        if (s[0] == '0')
        {
            return 0;
        }

        num[0] = 1;
        
        if (s[0] == '1' || s[0] == '2')
        {
            int prev = s[0] - '0';
            int curr = s[1] - '0';
            if (curr == 0 || prev * 10 + curr > 26)
            {
                num[1] = 1;
            }
            else
            {
                num[1] = 2;
            }
        }
        else
        {
            if (s[1] == '0')
            {
                return 0;
            }
            num[1] = 1;
        }
        for (int i = 2; i < length; i++)
        {
            int prev = s[i - 1] - '0';
            int curr = s[i] - '0';
            if (prev == 1 || prev == 2)
            {
                if (curr == 0)
                {
                    num[i] = num[i - 2];
                }
                else if (prev * 10 + curr > 26) {
                    num[i] = num[i - 1];
                }
                else
                {
                    num[i] = num[i - 1] + num[i - 2];
                }
            }
            else
            {
                if (curr == 0)
                {
                    return 0;
                }
                num[i] = num[i - 1];
            }
        }
        return num[length - 1];
    }
};