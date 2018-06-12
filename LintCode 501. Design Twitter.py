'''
Definition of Tweet:
class Tweet:
    @classmethod
    def create(cls, user_id, tweet_text):
         # This will create a new tweet object,
         # and auto fill id
'''
from collections import deque


class MiniTwitter:
    def __init__(self):
        self.twitters = deque()
        self.relations = {}
        self.selffeeds = {}

    """
    @param: user_id: An integer
    @param: tweet_text: a string
    @return: a tweet
    """

    def postTweet(self, user_id, tweet_text):
        twitter = Tweet.create(user_id, tweet_text)
        self.twitters.appendleft(twitter)
        if user_id in self.selffeeds:
            self.selffeeds[user_id].appendleft(twitter)
        else:
            self.selffeeds[user_id] = deque([twitter])
        return twitter

    """
    @param: user_id: An integer
    @return: a list of 10 new feeds recently and sort by timeline
    """

    def getNewsFeed(self, user_id):
        result = []
        friends = []
        if user_id in self.relations:
            friends = self.relations[user_id]
        for t in self.twitters:
            if t.user_id == user_id or t.user_id in friends:
                result.append(t)
                if len(result) == 10:
                    return result
        return result

    """
    @param: user_id: An integer
    @return: a list of 10 new posts recently and sort by timeline
    """

    def getTimeline(self, user_id):
        result = []
        if user_id in self.selffeeds:
            for t in self.selffeeds[user_id]:
                result.append(t)
                if len(result) == 10:
                    return result
        return result

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def follow(self, from_user_id, to_user_id):
        if from_user_id in self.relations:
            self.relations[from_user_id].append(to_user_id)
        else:
            self.relations[from_user_id] = [to_user_id]

    """
    @param: from_user_id: An integer
    @param: to_user_id: An integer
    @return: nothing
    """

    def unfollow(self, from_user_id, to_user_id):
        self.relations[from_user_id].remove(to_user_id)