class MedianFinder:

    def __init__(self):
        self.top = []
        self.bottom = [] # should be negative
        heapq.heapify(self.top)
        heapq.heapify(self.bottom)

    def addNum(self, num: int) -> None:
        if not self.bottom:
            heapq.heappush(self.bottom, -num)
            return
        if num <= -self.bottom[0]:
            heapq.heappush(self.bottom, -num)
        else:
            heapq.heappush(self.top, num)
        if len(self.bottom) - len(self.top) >= 2:
            while len(self.bottom) - len(self.top) >= 2:
                entry = heapq.heappop(self.bottom)
                heapq.heappush(self.top, -entry)
        elif len(self.top) - len(self.bottom) >= 2:
            while len(self.top) - len(self.bottom) >= 2:
                entry = heapq.heappop(self.top)
                heapq.heappush(self.bottom, -entry)

        print(self.bottom, self.top)

    def findMedian(self) -> float:
        if len(self.bottom) == len(self.top):
            return (-self.bottom[0] + self.top[0]) / 2
        elif len(self.bottom) > len(self.top):
            return -self.bottom[0]
        else:
            return self.top[0]
        