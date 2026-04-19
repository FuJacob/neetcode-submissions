class Twitter:
    """

issue, materialzied feeds  prnie to lots of update and satleness
shoul build on demand

each user has list of own tweets
each user has set of people they follow incl t hemselves

global timestmap increment per tweet

getnewsfeed, merge most recent tweets from all follwoed users using a max hepheap

take top 10




    """

    def __init__(self):
        self.time = 0
        self.user_to_tweets = defaultdict(list)
        self.user_to_following = defaultdict(set)
    

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.user_to_tweets[userId].append((-self.time, tweetId))
        self.time +=1
        
    def getNewsFeed(self, userId: int) -> List[int]:
        self.user_to_following[userId].add(userId)
        max_heap = []
        for followeeId in self.user_to_following[userId]:
            tweets = self.user_to_tweets[followeeId]
            if tweets:
                heapq.heappush(max_heap, (tweets[-1][0], tweets[-1][1], followeeId, len(tweets) - 1))
        feed = []
        
        while len(feed) != 10 and max_heap:
            _, tweetId, followeeId, idx = heapq.heappop(max_heap)
            feed.append(tweetId)
            if idx != 0:
                nxt_tweet = self.user_to_tweets[followeeId][idx-1]
                heapq.heappush(max_heap, (nxt_tweet[0], nxt_tweet[1], followeeId, idx-1))
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].add(followeeId)



    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_to_following[followerId].discard(followeeId)

        
