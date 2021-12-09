class Twitter:

    def __init__(self):
        self.hashmap = {}
        self.tweets = []

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append([userId, tweetId])
        
    def getNewsFeed(self, userId: int) -> List[int]:
        returned = []
        followed = {}
        if userId in self.hashmap:
            followed = self.hashmap[userId]
        for i in range(len(self.tweets)):
            if self.tweets[i][0] in followed: 
                returned.insert(0,self.tweets[i][1])
            elif userId == self.tweets[i][0]:
                returned.insert(0,self.tweets[i][1])
            if len(returned) == 11: 
                returned.pop(-1)
        return returned

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.hashmap: 
            self.hashmap[followerId] = {followeeId}
        else: 
            self.hashmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.hashmap:
            self.hashmap[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)