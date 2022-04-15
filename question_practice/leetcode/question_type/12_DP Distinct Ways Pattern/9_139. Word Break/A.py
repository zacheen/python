# My_v2  Runtime: 35 ms, faster than 95.90% of Python3
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

# given ans
# 完美的縮寫 (O)
class Solution:
    def wordBreak(self, s, wordDict):
        wordSet = set(wordDict)

        @lru_cache(None)  # 因為尾端比較常被呼叫到
        def wordBreak(s):
            if s in wordSet:
                return True
            return any(s[:i] in wordSet and wordBreak(s[i:]) for i in range(len(s)))

        return wordBreak(s)

s = Solution()
print(s.wordBreak(
    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
, wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa"]))
# print(s.wordBreak(
#     s = "leetcod"
# , wordDict = ["leet","cod"]))