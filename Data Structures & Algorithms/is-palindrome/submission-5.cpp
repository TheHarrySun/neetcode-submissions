class Solution {
public:
    bool isPalindrome(string s) {
        int first = 0;
        int end = s.length() - 1;
        while (first < end) {
            if (!((tolower(s[first]) - 'a') >= 0 && (tolower(s[first]) - 'a') < 26)) {
                if (!(s[first] - '0' >= 0 && s[first] - '0' <= 9)) {
                    first++;
                    continue;
                }
            }
            if (!((tolower(s[end]) - 'a') >= 0 && (tolower(s[end]) - 'a') < 26)) {
                if (!(s[first] - '0' >= 0 && s[first] - '0' <= 9)) {
                    end--;
                    continue;
                }
            }
            if (tolower(s[end]) == tolower(s[first])) {
                end--;
                first++;
            }
            else {
                return false;
            }
        }
        return true;
    }
};
