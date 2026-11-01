
import heapq

class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.time += 1

        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        users = self.following.get(userId, set()).copy()
        users.add(userId)

        all_tweets = []

        for user in users:
            for time, tweetId in self.tweets.get(user, []):
                all_tweets.append((time, tweetId))

        all_tweets.sort(reverse=True)

        return [tweetId for time, tweetId in all_tweets[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = set()

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
