class Solution {
public:
    int trap(vector<int>& height) {
        int n = height.size();
        int water = 0;
        int first;
        int last;
        vector<int> prefix;
        vector<int> suffix;
        prefix.push_back(height[0]);
        int pref = height[0];
        for (int i = 1; i < n; i++) {
            if (height[i] > pref) {
                prefix.push_back(height[i]);
                pref = height[i];
            }
            else {
                prefix.push_back(pref);
            }
        }
        int suff = height[n - 1];
        suffix.push_back(suff);
        for (int i = n - 2; i >= 0; i--) {
            if (height[i] > suff) {
                suffix.push_back(height[i]);
                suff = height[i];
            }
            else {
                suffix.push_back(suff);
            }
        }
        reverse(suffix.begin(), suffix.end());

        for (int i = 0; i < n; i++) {
            int temp = min(prefix[i], suffix[i]);
            if (temp > height[i]) {
                water += temp - height[i];
            }
        }
        return water;
    }
};
