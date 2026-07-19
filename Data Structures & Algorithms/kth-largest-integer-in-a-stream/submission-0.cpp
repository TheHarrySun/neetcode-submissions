class KthLargest
{
    int k;
    priority_queue<int, vector<int>, greater<int>> minHeap;

public:
    KthLargest(int k, vector<int> &nums)
    {
        this->k = k;
        for (int i : nums)
        {
            this->minHeap.push(i);
            if (minHeap.size() > k)
            {
                minHeap.pop();
            }
        }
    }

    int add(int val)
    {
        this->minHeap.push(val);
        if (minHeap.size() > k)
            minHeap.pop();
        return minHeap.top();
    }
};