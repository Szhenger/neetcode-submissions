class Twitter:

    def __init__(self):
        self.tweetCnt = 0
        self.tweetMap = defaultdict(list) # userId -> list of [tweetCnt, tweetId]
        self.followMap = defaultdict(set) # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetCnt += 1
        self.tweetMap[userId].append([self.tweetCnt, tweetId]) 

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        self.followMap[userId].add(userId)
        for followeeId in self.followMap[userId]:
            if followeeId in self.tweetMap:
                index = len(self.tweetMap[followeeId]) - 1
                count, tweet = self.tweetMap[followeeId][index]
                maxHeap.append([count, tweet, followeeId, index - 1])
        self.followMap[userId].remove(userId)
        heapq.heapify_max(maxHeap)
        
        feed = []
        while maxHeap and len(feed) < 10:
            count, tweet, followee, index = heapq.heappop_max(maxHeap)
            feed.append(tweet)
            if index >= 0:
                count, tweet = self.tweetMap[followee][index]
                heapq.heappush_max(maxHeap, [count, tweet, followee, index - 1])
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        
