class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> seen;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            seen[nums[i]] = i;
        }
        for (int i = 0; i < nums.size(); i++) {
            int temp = target - nums[i];
            if (seen.count(temp) && i != (seen.find(temp))->second) {
                ans.push_back(i);
                ans.push_back((*seen.find(temp)).second);
                return ans;
            }
        }
        return ans;
    }
};
