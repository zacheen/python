# given ans 使用 DP
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        isPalindrome = lambda s : s == s[::-1] 

        # 裡面存到目前第N個位置為止 有可能的組合
        dp = [[] for _ in range(len(s)+1)]
        print(dp)
        for i in range(1, len(s)+1):
            for j in range(i):
                if isPalindrome(s[j:i]):
                    if len(dp[j]) > 0:
                        for l in dp[j]:
                            dp[i].append(l+[s[j:i]])
                    else:
                        dp[i].append([s[j:i]])
        print(dp)
        return dp[-1]
                        

# given ans 算是使用 recursion
# class Solution:
#     def partition(self, s):
#         def helper(s, path) :
#             print(s, path)
#             if not s: # 傳進來字串為空的 # 代表到底了
#                 res.append(path)
#                 return
#             for i in range(1, len(s) + 1 ) :
#                 front = s[:i]
#                 if isPalindrome(front) :
#                     helper(s[i:], path+[front])

#         # 這個比較快...
#         isPalindrome = lambda s : s == s[::-1] 
#         # def isPalindrome(regular):
#         #     print("<"+regular+">")
#         #     totalLen = len(regular)
#         #     mid = totalLen // 2
#         #     MaxIdx = totalLen - 1
#         #     for i in range(mid):
#         #         if regular[i] != regular[MaxIdx-i] :
#         #             return False
#         #     return True
#         res = []
#         helper(s, [])
#         return res

# 應該要弄一個 如果是isPalindrome 有什麼可能的組合的 cache 版本 ??
# 有 cache 版本 但速度沒什麼差
# class Solution:
#     def partition(self, s):
#         cache = {}
#         def helper(s, path) :
#             if not s:
#                 res.append(path)
#                 return
#             for i in range(1, len(s) + 1 ) :
#                 front = s[:i]
#                 # print(front)
#                 haveCache = cache.get(front, None) 
#                 if haveCache == None :
#                     if isPalindrome(front) :
#                         helper(s[i:], path+[front])
#                 elif haveCache :
#                     helper(s[i:], path+[front])

#         # isPalindrome = lambda s : s == s[::-1] 
#         def isPalindrome(regular):
#             print("<"+regular+">")
#             totalLen = len(regular)
#             mid = totalLen // 2
#             MaxIdx = totalLen - 1
#             for i in range(mid):
#                 if regular[i] != regular[MaxIdx-i] :
#                     cache[regular] = False
#                     return False
#             cache[regular] = True
#             return True

        # res = []
        # helper(s, [])
        # return res

s = Solution()
print(s.partition("aabbb"))