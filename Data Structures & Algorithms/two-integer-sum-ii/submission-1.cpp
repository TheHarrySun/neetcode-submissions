class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int n = numbers.size();
        int first = 0;
        int last = n - 1;
        int ans = numbers[first] + numbers[last];
        while(ans != target) {
            if (ans > target) {
                last--;
            }
            else {
                first++;
            }
            ans = numbers[first] + numbers[last];
        }
        return {first + 1, last + 1};
    }
};
