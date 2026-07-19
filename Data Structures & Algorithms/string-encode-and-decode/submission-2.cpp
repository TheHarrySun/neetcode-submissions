class Solution {
public:

    string encode(vector<string>& strs) {
        string ans;
        for (int i = 0; i < strs.size(); i++) {
            ans = ans + to_string(strs[i].length()) + "#" + strs[i];
        }
        return ans;
    }

    vector<string> decode(string s) {
        vector<string> ans;
        int i = 0;
        while (i < s.length()) {
            int j = i;
            while (s[j] != '#') {
                j++;
            }
            int length = stoi(s.substr(i, j - i));
            j++;
            ans.push_back(s.substr(j, length));
            i = j + length;
        }
        return ans;
    }
};
