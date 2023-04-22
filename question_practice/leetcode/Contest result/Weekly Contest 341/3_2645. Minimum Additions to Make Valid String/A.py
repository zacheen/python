from typing import List
import functools

# my Beats 55.77%
class Solution:
    def addMinimum(self, word: str) -> int:
        ans = 0
        # 開頭一定要補齊 a 最後一定要補齊 c
        last_word = "c"
        word = word + "a" 
        order = ["a","b","c","a","b","c"]
        for now_c in word :
            last_word_indx = order.index(last_word)
            last_word_indx += 1
            while(True) :
                if order[last_word_indx] == now_c :
                    break
                else :
                    last_word_indx += 1
                    ans += 1
            last_word = now_c
        return ans
            

# # given ans Beats 41.75% 
#     # 速度較慢 畢竟因為才3個字母而已
#     # 所以我 while 還比較快
# # 我是用 while 計算要加入幾個字
# # 有人直接用算的
#     # 不過補開頭跟結尾的想法跟我一樣
# class Solution:
#     def addMinimum(self, word: str) -> int:
#         ans = 0
#         # 開頭一定要補齊 a 最後一定要補齊 c
#         last_word = "c"
#         word = word + "a" 
        
#         # 這裡我有再優化
#         @functools.lru_cache(None)
#         def cal_dis(last_w, now_w) :
#             dis = ord(now_w) - ord(last_w) -1
#             if dis < 0 :
#                 return dis + 3
#             else :
#                 return dis

#         for now_c in word :
#             ans += cal_dis(last_word, now_c)
#             last_word = now_c
        
#         return ans

# given ans
# 還有人直接把各種組合的距離列出來

s = Solution()
print(s.addMinimum("b"))
print(s.addMinimum("aaa"))
print(s.addMinimum("abc"))



