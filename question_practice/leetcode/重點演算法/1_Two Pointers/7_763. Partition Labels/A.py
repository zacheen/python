# My v1 Runtime: 100 ms, faster than 6.83% of Python3
# class Solution:
#     def partitionLabels(self, s):
#         # 想法
#         # 抓一個近來 找此字母最尾端
#         # 找此list的下一個字母 也是找最尾端
#         # 找過的字加到 mem
#         # 直到 此 list 到尾端
        
#         strat_indx = 0
#         ans = []
#         while strat_indx < len(s) :
#             this_part = list(s[strat_indx])
#             end_indx = strat_indx+1
#             mem = set()
#             for each_word in this_part :
#                 print("find :", each_word)
#                 if each_word in mem :
#                     continue
#                 mem.add(each_word)
#                 back_indx = len(s)-1
#                 while back_indx >= end_indx :
#                     print(back_indx, s[back_indx], end_indx, s[back_indx])
#                     if s[back_indx] == each_word :
#                         print("extend :", s[end_indx:back_indx+1])
#                         this_part.extend(s[end_indx:back_indx+1])
#                         end_indx = back_indx+1
#                         break
#                     back_indx -= 1

#             print("for end :", this_part)
            
#             strat_indx += len(this_part)        
#             ans.append(len(this_part))
        
#         return ans

# My v2 一開始就先找各個字的最尾端
# Runtime: 67 ms, faster than 33.23% of Python3
# class Solution:
#     def partitionLabels(self, s):
#         # 找各個字母最後的位置
#         last_place = {}
#         indx = len(s)-1
#         for w in reversed(s) :
#             ret = last_place.get(w, None)
#             if ret == None :
#                 last_place[w] = indx
#             indx -= 1
#         # print(last_place)

#         strat_indx = 0
#         ans = []
#         while strat_indx < len(s) :
#             this_part = list(s[strat_indx])
#             end_indx = strat_indx+1
#             mem = set()
#             for each_word in this_part :
#                 # print("find :", each_word)
#                 if each_word in mem :
#                     continue
#                 mem.add(each_word)
#                 if last_place[each_word] >= end_indx :
#                     print("extend :", s[end_indx:last_place[each_word]+1])
#                     this_part.extend(s[end_indx:last_place[each_word]+1])
#                     end_indx = last_place[each_word]+1

#             # print("for end :", this_part)
            
#             strat_indx += len(this_part)        
#             ans.append(len(this_part))
        
#         return ans

# given ans            
class Solution:
    def partitionLabels(self, S):
        ans = []
        # 對 其實直接覆寫就好了 ...
        # 如果 上面的 code 改成這樣 Runtime: 48 ms, faster than 72.59% of Python3
        last_place = {c: i for i, c in enumerate(S)}

        l = 0
        r = 0
        for i, c in enumerate(S):
            r = max(r, last_place[c])
            # 這個判斷太神了 當indx追到目前最後面的字的位置 代表這個是可以切開的位置
            if i == r:
                ans.append(r - l + 1)
                l = r + 1

        return ans

s = Solution()
print(s.partitionLabels("ababcbacadefegdehijhklij"))
# print(s.partitionLabels("abcabcdefdef"))
