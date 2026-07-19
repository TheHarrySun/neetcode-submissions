class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        int maxlength = 0;
        int first = 0;
        int end = 0;
        unordered_set<char> substring;
        while (first <= end && end < s.length()) {
            if (substring.count(s[end])) {
                maxlength = max(maxlength, end - first);
                while (s[first] != s[end]) {
                    substring.erase(s[first]);
                    first++;
                }
                first++;
                end++;
            }
            else {
                substring.insert(s[end]);
                end++;
            }
        }
        maxlength = max(maxlength, end - first);
        return maxlength;
    }
};
