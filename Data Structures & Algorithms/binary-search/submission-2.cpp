class Solution {
public:
    int search(vector<int>& nums, int target) {
        int n = nums.size();
        int bot = 0;
        int top = n - 1;
        while (bot != top) {
            int index = (bot + top) / 2;
            if (nums[index] == target) {
                return index;
            }
            else if (nums[index] < target) {
                bot = index + 1;
            }
            else {
                top = index;
            }
        }
        if (target == nums[bot]) {
            return bot;
        }
        return -1;
    }
};
