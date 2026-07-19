class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_set<int> freq(nums.begin(), nums.end());
        int ans = 0;
        vector<int> starts;
        for (int i = 0; i < nums.size(); i++) {
            if (!freq.count(nums[i] - 1)) {
                int dist = 1;
                while (freq.find(nums[i] + dist) != freq.end()) {
                    dist ++;
                }
                ans = max(dist, ans);
            }
        }
        return ans;
    }
};
