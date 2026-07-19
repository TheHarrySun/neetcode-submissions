class MedianFinder
{
    priority_queue<int> bottomheap;
    priority_queue<int, vector<int>, greater<int>> topheap;
    int count;

public:
    MedianFinder()
    {
        count = 0;
    }

    void addNum(int num)
    {
        bottomheap.push(num);
        if (!topheap.empty() && bottomheap.top() > topheap.top())
        {
            topheap.push(bottomheap.top());
            bottomheap.pop();
        }
        if (bottomheap.size() > 1 + topheap.size())
        {
            int temp = bottomheap.top();
            bottomheap.pop();
            topheap.push(temp);
        }
        else if (topheap.size() > 1 + bottomheap.size())
        {
            int temp = topheap.top();
            topheap.pop();
            bottomheap.push(temp);
        }
        count++;
    }

    double findMedian()
    {
        if (count % 2 == 0)
        {
            return (bottomheap.top() + topheap.top()) / 2.0;
        }
        else
        {
            if (bottomheap.size() > topheap.size())
            {
                return bottomheap.top();
            }
            else
            {
                return topheap.top();
            }
        }
    }
};