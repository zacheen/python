# My_v2  Time Limit Exceeded
class Solution:
    def wordBreak(self, s, wordDict):
        cache = [False]* (len(s)+1)
        cache[0] = True
        def find(remainstr, index):
            if remainstr == "" :
                return True

            if cache[index] :
                return False
            
            for eachWord in wordDict :
                fit = True
                for i in range(len(eachWord)) :
                    if i>=len(remainstr) or eachWord[i] != remainstr[i] :
                        fit = False
                        break
                if fit :
                    cache[index] = True
                    if find(remainstr[len(eachWord):], index+len(eachWord)) :
                        return True

            return False

        return find(s, 1)

# My_v1  Time Limit Exceeded  
# My_v1 如果 'a' + 'a' 不行 我還會用 'aa' 再嘗試一次
# class Solution:
#     def wordBreak(self, s, wordDict):
#         def find(remainstr):
#             if remainstr == "" :
#                 return True
            
#             for eachWord in wordDict :
#                 fit = True
#                 for i in range(len(eachWord)) :
#                     if i>=len(remainstr) or eachWord[i] != remainstr[i] :
#                         fit = False
#                         break
#                 if fit :
#                     if find(remainstr[len(eachWord):]) :
#                         return True

#             return False

#         return find(s)
            
# class Solution:
#     def wordBreak(self, s, wordDict): 
#         L = len(s)
#         # 紀錄到第幾個字是OK的
#         # 我上面的 如果 'a' + 'a' 不行 我還會用 'aa' 再嘗試一次
#         dp = [False]*(L+1)
#         dp[0]=True
#         for i in range(1,L+1):
#             for j in range(i):
#                 if dp[j] and s[j:i] in wordDict:
#                     print(s[j:i])
#                     dp[i] = True
#         print(dp)
#         return dp[-1]

s = Solution()
print(s.wordBreak(
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
, wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa"]))
# print(s.wordBreak(
#     s = "leetcod"
# , wordDict = ["leet","cod"]))