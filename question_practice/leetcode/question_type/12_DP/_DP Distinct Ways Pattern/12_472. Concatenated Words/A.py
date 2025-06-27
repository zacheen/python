# 472. Concatenated Words
# https://leetcode.com/problems/concatenated-words

# my Time Limit Exceeded
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words):
#         empty_str = False

#         while True :
#             try :
#                 words.remove("")
#                 # empty_str = True
#             except ValueError :
#                 break
        
#         def cut(word, count) :
#             # print(word)
#             if word == "" :
#                 if count >= 2 or empty_str :
#                     return True
#                 else :
#                     return False
            
#             for w in words :
#                 if len(w)<=len(word) and word[:len(w)] == w :
#                     if cut(word[len(w):], count+1) :
#                         return True
#             return False
        
#         ans = []
#         for w in words :
#             if cut(w, 0) :
#                 ans.append(w)
#         return ans

# given ans
# Runtime: 392 ms, faster than 91.21% of Python3
# 我概念是對的 但優化問題 我沒有想到in會這麼快
# 會快這麼多也許也是因為 @lru_cache 因為短的比較常呼叫到
# class Solution:
#     def findAllConcatenatedWordsInADict(self, words):
#         wordSet = set(words)

#         # @lru_cache(None)
#         def isConcat(word):
#             for i in range(1, len(word)):  # 從1開始是為了排除空字串的問題
#                 prefix = word[:i]
#                 suffix = word[i:]
#                 if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
#                     return True

#             return False

#         return [word for word in words if isConcat(word)]

# 只記錄對的答案 好像會快一點點
# Runtime: 388 ms, faster than 92.20% of Python3
class Solution:
    def findAllConcatenatedWordsInADict(self, words):
        wordSet = set(words)

        ans_set = set()
        def isConcat(word):
            if word in ans_set:
                return True
            
            for i in range(1, len(word)):  # 從1開始是為了排除空字串的問題
                prefix = word[:i]
                suffix = word[i:]
                if prefix in wordSet and (suffix in wordSet or isConcat(suffix)):
                    ans_set.add(word)
                    return True

            return False

        return [word for word in words if isConcat(word)]

s = Solution()
# print(s.findAllConcatenatedWordsInADict(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
print(s.findAllConcatenatedWordsInADict(["rfkqyuqfjkx","","vnrtysfrzrmzl"]))
# print(s.findAllConcatenatedWordsInADict(["cat","","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
# print(s.findAllConcatenatedWordsInADict(["a","b","c","d","af","abc","acb","aca","afd","adbc"]))


