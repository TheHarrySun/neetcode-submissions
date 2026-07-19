class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> triplets;
        int n = nums.size();
        sort(nums.begin(), nums.end());
        for (int i = 0; i < n - 2; i++) {
            if (nums[i] > 0) {
                break;
            }
            if (i > 0 && nums[i] == nums[i-1]) {
                continue;
            }
            int first = i + 1;
            int end = n - 1;
            while (first < end) {
                int sum = nums[first] + nums[end];
                if (sum == -1 * nums[i]) {
                    triplets.push_back({nums[i], nums[first], nums[end]});
                    end--;
                    first++;
                    while (first < end) {
                        if (nums[end] == nums[end + 1]) {
                            end--;
                        }
                        else {
                            break;
                        }
                    }
                }
                else if (sum > -1 * nums[i]) {
                    end--;
                }
                else {
                    first++;
                }
            }
        }   
        return triplets;     
    }
};
