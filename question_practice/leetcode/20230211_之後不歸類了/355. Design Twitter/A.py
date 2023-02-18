# my 
class Twitter(object):

    def __init__(self):
        # dir map

        # post_order
        post_mem = deque()
        

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        post_mem.加入前面( (userId , tweetId) )

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        return_list = []
        for mem_userId, tweetId in post_mem :
            if mem_userId 屬於 userId :
                return_list.append(tweetId)
            if len(return_list) == 0 :
                return return_list
        

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # 加入 set
        

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        # 移除 set
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

# given ans

s = Solution()
print(s.())



