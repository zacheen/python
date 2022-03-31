# my v1 fail  沒考慮到 ("ABBB",2) 這種情況
# class Solution:
#     def characterReplacement(self, s, k):
#         count = []
#         word_list = []
#         last_word = s[0]
#         number = 0
#         for each_word in s :
#             if each_word == last_word :
#                 number += 1
#             else :
#                 count.append(number)
#                 word_list.append(last_word)
#                 last_word = each_word
#                 number = 1
#         count.append(number)
#         word_list.append(last_word)
#         print(count)
#         print(word_list)

#         max_len = 0
#         # l = 0
#         for l, each_word in enumerate(word_list) :
#             now_total = 0
#             remain_replace = k
#             r = l
#             while r < len(word_list) :
#                 now_total += count[r]
#                 if word_list[r] != each_word :
#                     remain_replace -= count[r]
#                     if remain_replace < 0 :
#                         break
#                 r += 1
#                 max_len = max(now_total, max_len)

#         return max_len

# my v2 fail
# 沒想到 (s = "aabbbaa", k = 1) 這種case
# 有可能只抓到一組字的其中一個字進來
# 不要把問題複雜化 
# from collections import Counter
# # My v2 判斷改用 count 取 max -> total - max對應的數量
# class Solution:
#     def characterReplacement(self, s, k):
#         count = []
#         word_list = []
#         last_word = s[0]
#         number = 0
#         for each_word in s :
#             if each_word == last_word :
#                 number += 1
#             else :
#                 count.append(number)
#                 word_list.append(last_word)
#                 last_word = each_word
#                 number = 1
#         count.append(number)
#         word_list.append(last_word)
#         print(count)
#         print(word_list)

#         max_len = 0
#         l = 0
#         now_total = 0
#         now_count = Counter()
#         for r, n in enumerate(count) :
#             now_total += n
#             now_count[word_list[r]] += n

#             # 找目前最多的字
#             most_common_word = now_count.most_common(1)[0][0]
#             # 其他字的數量 如果>k  l開始右移 
#             while now_total - now_count[most_common_word] > k :
#                 print(l,r,most_common_word)
#                 now_count[word_list[l]] -= count[l]
#                 now_total -= count[l]
#                 l += 1
#                 most_common_word = now_count.most_common(1)[0][0]  # 避免 "AAABBC" + "A"

#             max_len = max(max_len, now_total)

#         return max_len

# My v3 Runtime: 711 ms, faster than 5.02% of Python3
# from collections import Counter         
# class Solution:
#     def characterReplacement(self, s, k):
#         max_len = 0
#         l = 0
#         now_total = 0
#         now_count = Counter()
#         for r, r_word in enumerate(s) :
#             now_total += 1
#             now_count[r_word] += 1

#             # 找目前最多的字
#             most_common_word = now_count.most_common(1)[0][0]
#             # 其他字的數量 如果>k  l開始右移 
#             while now_total - now_count[most_common_word] > k :
#                 # print(l,r,most_common_word)
#                 now_count[s[l]] -= 1
#                 now_total -= 1
#                 l += 1
#                 most_common_word = now_count.most_common(1)[0][0]  # 避免 ("ABBB",0) 這種情況
#             max_len = max(max_len, now_total)
#         return max_len

# given ans
# Runtime: 132 ms, faster than 83.64% of Python3
from collections import Counter                 
class Solution:
    def characterReplacement(self, s, k):
        ans = 0
        maxCount = 0
        count = Counter()

        l = 0
        for r, c in enumerate(s):
            count[c] += 1
            # 這個是我們目前找到 最多字母重複的次數
            maxCount = max(maxCount, count[c])
            # 因為目前我們已經找到 最短有可能的長度 所以l縮到最短 不用小於此長度
            # 最短有可能的長度 : maxCount + k = 最多字母重複的次數 + 可以變換的字母數
            # 答案其實 = 某個區間字母重複的最多次數+可以變換的字母數(如果有其他空間可以變換)
            while maxCount + k < r - l + 1:
                count[s[l]] -= 1
                l += 1
            # (O) 這個演算法能成功的關鍵 : 就算答案不對 反正也不會比較長 所以不用特別處理 
            ans = max(ans, r - l + 1)

        return ans
        
# 另外一種解釋是 
# 現在這個區間有多少個字母需要變換 = 現在長度 - 之前計算過最大重複字母次數
# 如果不符合上面的結果 我們就不要增加長度 此結果就不會被記錄

s = Solution()
# print(s.characterReplacement("AABABBA",1))
# print(s.characterReplacement(s = "BBAABABBAAABB", k = 2))
print(s.characterReplacement("ABBB",0))
# print(s.characterReplacement(s = "ABABABABAB", k = 4))
# print(s.characterReplacement(s = "AAABAAABBAAABBAAABBBAAA", k = 2))
# print(s.characterReplacement(s = "aabbbaa", k = 1))
# print(s.characterReplacement(s = "AAABBCA", k = 1))
