using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }
        unordered_map<char, int> mapping_s;
        unordered_map<char, int> mapping_t;
        for (int i = 0; i < s.size(); i++) {
            mapping_s[s[i]]++;
            mapping_t[t[i]]++;
        }
        return mapping_s == mapping_t;
    }
};
