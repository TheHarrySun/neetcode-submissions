class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int res = nums[0];
        int currMin = 1;
        int currMax = 1;

        for (int num: nums) {
            int tmp = currMax * num;
            currMax = max(currMax * num, max(currMin * num, num));
            currMin = min(currMin * num, min(tmp, num));
            res = max(currMax, res);
        }
        return res;
    }
};
