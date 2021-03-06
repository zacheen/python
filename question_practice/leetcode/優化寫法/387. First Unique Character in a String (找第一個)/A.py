# given ans 
# class Solution:
#     def firstUniqChar(self, s):
#         # build hash map : character and how often it appears
#         from collections import Counter
#         count = Counter(s)
#         print(count)
        
#         # 如果是要回傳字 危險用法 但第一個一定是
#         # for eachChar in count :
#         #     # print(eachChar, count[eachChar])
#         #     if count[eachChar] == 1 :
#         #         return eachChar  

#         # find the index
#         # (O)
#         for idx, ch in enumerate(s):
#             if count[ch] == 1:
#                 return idx     
#         return -1

# My 跟 given ans 概念是一樣的
# class Solution:
#     def firstUniqChar(self, s):
        
#         pos = {}
#         cache = {}
        
#         for i in range(len(s)) :
#             eachCard = s[i]
#             inCache = cache.get(eachCard, None)
#             if inCache == None :
#                 cache[eachCard] = 1
#                 pos[eachCard] = i
#             else :
#                 cache[eachCard] = 2
                
#         print(cache)
#         # 雖然有點危險...
#         for item in cache.items():
#             if item[1] == 1:
#                 return pos[item[0]]
#         return -1

# 2022 05 21 再次練習
# my Runtime: 232 ms, faster than 22.91% of Python3
# class Solution:
#     def firstUniqChar(self, s):
#         stack = []
#         count = Counter()
#         for i,c in enumerate(s) :
#             if count[c] == 0 :
#                 stack.append((i,c))
#                 count[c] = 1
#             else :
#                 count[c] += 1
                
#         for i,c in stack :
#             if count[c] == 1 :
#                 return i
#         return -1

# given ans
class Solution:
    def firstUniqChar(self, s):
        count = Counter(s)

        for i, c in enumerate(s):
            if count[c] == 1:
                return i

        return -1

s = Solution()
print(s.firstUniqChar("loveleetcode"))
# print(s.firstUniqChar("aabb"))