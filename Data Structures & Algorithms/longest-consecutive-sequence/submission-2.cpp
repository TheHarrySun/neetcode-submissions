class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> freq(nums.begin(), nums.end());
        int max = 0;
        vector<int> starts;
        for (int i = 0; i < nums.size(); i++) {
            if (!freq.count(nums[i] - 1)) {
                starts.push_back(nums[i]);
            }
        }
        for (int i = 0; i < starts.size(); i++) {
            int dist = 1;
            for (int j = 1; j < nums.size(); j++) {
                if (freq.count(starts[i] + j)) {
                    dist++;
                }
                else {
                    break;
                }
            }
            if (dist > max) {
                max = dist;
            }
        }
        return max;
    }
};
