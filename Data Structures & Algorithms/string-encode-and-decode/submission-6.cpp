class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string s : strs) {
            res += to_string(s.size()) + '#' + s;
        }
        return res;
    }

    vector<string> decode(string s) {
        int start = 0;
        vector<string> ans;
        while (start < s.size()) {
            int end = start;
            while (s[end] != '#') {
                end++;
            }
            int length = stoi(s.substr(start, end - start));
            start = end + 1;
            string word = s.substr(start, length);
            ans.push_back(word);
            start = start + length;
        }
        return ans;
    }
};
