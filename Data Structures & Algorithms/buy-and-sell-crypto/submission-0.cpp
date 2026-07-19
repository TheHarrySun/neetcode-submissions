class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int smallest = prices[0];
        int ans = 0;
        for (int i = 1; i < prices.size(); i++) {
            ans = max(prices[i] - smallest, ans);
            if (prices[i] < smallest) {
                smallest = prices[i];
            }
        }
        return ans;
    }
};
