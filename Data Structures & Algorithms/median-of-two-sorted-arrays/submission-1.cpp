class Solution
{
public:
    double findMedianSortedArrays(vector<int> &nums1, vector<int> &nums2)
    {
        int total_size = nums1.size() + nums2.size();
        bool even = total_size % 2 == 0;
        int half = total_size / 2;
        int r = 0;
        int l = 0;
        int ans;
        for (int i = 0; i < half; i++)
        {
            if (l == nums1.size())
            {
                ans = nums2[r];
                r++;
            }
            else if (r == nums2.size())
            {
                ans = nums1[l];
                l++;
            }
            else if (nums1[l] <= nums2[r])
            {
                ans = nums1[l];
                l++;
            }
            else
            {
                ans = nums2[r];
                r++;
            }
        }
        nums1.push_back(INT_MAX);
        nums2.push_back(INT_MAX);
        if (even)
        {
            return (ans + min(nums1[l], nums2[r])) / 2.0;
        }
        else
        {
            return min(nums1[l], nums2[r]);
        }
    }
};