class Twitter:

    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list) # userId -> list of [count, tweetIds]
        self.followMap = defaultdict(set) # userId -> set of [followeeIds]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.time, tweetId])
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        heapq.heapify(heap)
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            for tweets in self.tweetMap[followee]:
                heapq.heappush(heap, tweets)
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        for i in range(10):
            if heap:
                res.append(heapq.heappop(heap)[1])
        return res[::-1]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
