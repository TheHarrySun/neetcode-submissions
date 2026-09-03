class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> groups;
        for (string s : strs) {
            array<int, 26> count{};
            for (char c : s) {
                count[c - 'a']++;
            }
            string key = "";
            for (int i : count) {
                key += to_string(i) + ',';
            }
            groups[key].push_back(s);
        }
        vector<vector<string>> res;
        for (const auto& [key, val] : groups) {
            res.push_back(val);
        }
        return res;
    }
};
