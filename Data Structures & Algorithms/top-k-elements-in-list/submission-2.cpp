class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
         unordered_map<int, int> count;
         vector<vector<int>> sizes(nums.size() + 1);

         for (int i = 0; i < nums.size(); i++) {
            count[nums[i]] += 1;
         }
         for (auto& entry : count) {
            sizes[entry.second].push_back(entry.first);
         }
         vector<int> ans;
         for (int i = sizes.size() - 1; i > 0; i--) {
            for (int j : sizes[i]) {
                if (ans.size() == k) {
                    return ans;
                }
                ans.push_back(j);
            }
         }
         return ans;
    }
};
