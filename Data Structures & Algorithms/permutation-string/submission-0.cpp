class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        unordered_map<char, int> permutation;
        for (char c : s1) {
            permutation[c] += 1;
        }
        if (s2.length() < s1.length()) {
            return false;
        }
        
        int l = 0;
        for (int i = s1.length() - 1; i < s2.length(); i++) {
            unordered_map<char, int> temp;
            for (int j = l; j <= i; j++) {
                temp[s2[j]] += 1;
            }
            if (temp == permutation) {
                return true;
            }
            l++;
        }
        return false;
    }
};
