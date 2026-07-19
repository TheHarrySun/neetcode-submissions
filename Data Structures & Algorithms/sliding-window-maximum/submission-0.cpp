class Solution
{
public:
    vector<int> maxSlidingWindow(vector<int> &nums, int k)
    {
        priority_queue<pair<int, int>> pq;
        vector<int> ans;

        int l = 0;
        int r = k - 1;
        for (int i = 0; i <= r; i++)
        {
            pq.push({nums[i], i});
        }
        while (r < nums.size())
        {
            pair<int, int> num = pq.top();
            while (num.second < l)
            {
                pq.pop();
                num = pq.top();
            }
            ans.push_back(num.first);
            l++;
            r++;
            pq.push({nums[r], r});
        }
        return ans;
    }
};