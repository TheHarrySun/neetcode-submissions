class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<pair<int, int>> mapping;
        for (int i = 0; i < nums.size(); i++) {
            mapping.push_back(pair(nums[i], i));
        }
        sort(mapping.begin(), mapping.end());
        int l = 0;
        int r = nums.size() - 1;
        while (l < r) {
            int temp = mapping[l].first + mapping[r].first;
            if (temp == target) {
                if (mapping[l].second < mapping[r].second) 
                    return {mapping[l].second, mapping[r].second};
                return {mapping[r].second, mapping[l].second};                
            }
            else if (temp < target) {
                l++;
            }
            else {
                r--;
            }
        }
        return {l, r};
    }
};
