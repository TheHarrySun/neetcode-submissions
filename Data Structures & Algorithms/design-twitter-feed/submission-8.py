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
            if followee in self.tweetMap:
                index = len(self.tweetMap[followee]) - 1
                time, tId = self.tweetMap[followee][index]
                heapq.heappush(heap, [-time, tId, followee, index])
                if len(heap) > 10:
                    heapq.heappop(heap)
        res = []
        while heap and len(res) < 10:
            time, tId, followee, index = heapq.heappop(heap)
            res.append(tId)
            index -= 1
            if index >= 0:
                nTime, ntId = self.tweetMap[followee][index]
                heapq.heappush(heap, [-nTime, ntId, followee, index])
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
