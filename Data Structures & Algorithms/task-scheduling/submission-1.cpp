class Solution
{
public:
    int leastInterval(vector<char> &tasks, int n)
    {
        vector<int> counts(26, 0);
        for (char task : tasks)
        {
            counts[task - 'A']++;
        }

        priority_queue<int> maxheap;
        for (int count: counts) {
            if (count > 0) {
                maxheap.push(count);
            }
        }

        queue<pair<int, int>> q;
        int totaltime = 0;
        while (!maxheap.empty() || !q.empty())
        {
            totaltime += 1;

            if (maxheap.empty()) {
                totaltime = q.front().second;
            }
            else {
                int count = maxheap.top() - 1;
                maxheap.pop();
                if (count > 0) {
                    q.push({count, totaltime + n});
                }
            }

            if (!q.empty() && q.front().second == totaltime) {
                maxheap.push(q.front().first);
                q.pop();
            }
        }
        return totaltime;
    }
};