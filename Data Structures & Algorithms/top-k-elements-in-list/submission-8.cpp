class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        unordered_map<int, int> freq;
        for (int& num : nums) {
            freq[num] += 1;
        }
        for (const auto& [key, val] : freq) {
            buckets[val].push_back(key);
        }
        vector<int> res;
        for (int i = n; i >= 0; i--) {
            for (int num : buckets[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
        return res;
    }
};
