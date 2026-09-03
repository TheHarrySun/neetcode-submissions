class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        // this is linear time and doesn't require sorting
        unordered_map<int, int> indices;
        for (int i = 0; i < nums.size(); i++) {
            indices[nums[i]] = i;
        }

        for (int i = 0; i < nums.size(); i++) {
            int diff = target - nums[i];
            if (indices.contains(diff) && indices[diff] != i) {
                return {i, indices[diff]};
            }
        }
        return {-1, -1};
    }
};
