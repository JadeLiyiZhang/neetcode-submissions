class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetMap = defaultdict(list)
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        res = []
        self.followMap[userId].add(userId)
        for followerId in self.followMap[userId]:
            for count, id in self.tweetMap[followerId]:
                heapq.heappush(tweets, (count, id))
        for i in range(10):
            if tweets:
                count, id = heapq.heappop(tweets)
                res.append(id)
        return res
        


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
