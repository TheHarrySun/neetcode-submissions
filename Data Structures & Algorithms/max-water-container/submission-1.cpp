class Solution {
public:
    int maxArea(vector<int>& heights) {
        int n = heights.size();
        int first = 0;
        int last = n - 1;
        int max = 0;
        while (first < last) {
            int temp = (last - first) * min(heights[first], heights[last]);
            if (temp > max) {
                max = temp;
            }
            if (heights[first] <= heights[last]) {
                first++;
            }
            else {
                last--;
            }
        }
        return max;
    }
};
