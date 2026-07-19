class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> words;
        for (int i = 0; i < strs.size(); i++) {
            vector<int> count(26, 0);
            for (char s : strs[i]) {
                count[s - 'a']++;
            }
            string key = to_string(count[0]);
            for (int i = 1; i < 26; i++) {
                key = key + ',' + to_string(count[i]);
            }
            words[key].push_back(strs[i]);
        }
        vector<vector<string>> ans;
        for (auto& pair : words) {
            ans.push_back(pair.second);
        }
        return ans;
    }
};
