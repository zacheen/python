from collections import Counter
# My Runtime: 68 ms, faster than 93.53% of Python3
# class Solution:
#     def checkInclusion(self, s1, s2):
#         if len(s1) > len(s2):
#             return False
        
#         remain_s1 = Counter(s1)
#         remain_s1 = dict(remain_s1)
#         remain_match = len(remain_s1)

#         # 對 slide window 來說新增一個字母  
#         def add_word(w):
#             ret = remain_s1.get(w, None)
#             ret_match = remain_match
#             if ret != None :
#                 if ret == 1 :
#                     ret_match -= 1
#                 remain_s1[w]-=1 # 
#             return ret_match

#         def remove_word(w):
#             ret = remain_s1.get(w, None)
#             ret_match = remain_match
#             if ret != None :
#                 if ret == 0 :
#                     ret_match += 1
#                 remain_s1[w]+=1
#             return ret_match 

#         for i in range(len(s1)):
#             remain_match = add_word(s2[i])
#         # print(remain_s1)
        
#         if remain_match == 0 :
#             return True

#         for i in range(len(s2)-len(s1)):
#             remain_match = add_word(s2[i+len(s1)])
#             remain_match = remove_word(s2[i])
#             if remain_match == 0 :
#                 return True

#         return False

# function 測試code
        # print(remain_s1, remain_match)
        # remain_match = add_word("b")
        # print(remain_s1, remain_match)
        # remain_match = add_word("a")
        # print(remain_s1, remain_match)
        # remain_match = remove_word("b")
        # print(remain_s1, remain_match)
        # remain_match = remove_word("c")
        # print(remain_s1, remain_match)
        # remain_match = remove_word("c")
        # print(remain_s1, remain_match)

# given ans  Runtime: 84 ms, faster than 81.33% of Python3
# 我判斷有沒有符合條件是用 remain_match
# 他直接計數 目前符合的字母有幾個
class Solution:
    def checkInclusion(self, s1, s2):
        count = Counter(s1)
        required = len(s1)

        for r, c in enumerate(s2):
            print(r - len(s1), r, "新字:", c, "required:",required, count)
            # r 右移  此字母count 減少
            count[c] -= 1
            # (O) 優化演算法
            # count[c] >= 0 代表s1的字母set中有此字母 且此字母還沒有符合最終條件
            # 因為 count 是用倒數的方式
            # 所以那些原本就為0的數字 不管怎樣都不會 > 0
            # 我用 "get + 判斷取出數量" 實現  多了一個比較
            if count[c] >= 0:
                required -= 1
            # window 長度 已經到 s1 長度 所以要開始縮了 
            l = r - len(s1)
            if l >= 0:
                count[s2[l]] += 1
                # (O) 優化演算法 
                # 如果不是原本就有的計數的字母 根本不可能>0
                if count[s2[l]] > 0:  
                    required += 1
            # 這個不能擺在 r >= len(s1): 底下是因為要避免 ("a", "ab") 這種情況
            if required == 0:
                return True

        return False

s = Solution()
# print(s.checkInclusion(s1 = "ab", s2 = "eidbaooo"))
# print(s.checkInclusion(s1 = "ab", s2 = "eidboaoo"))
# print(s.checkInclusion(s1 = "ab", s2 = "a"))

# 為了看 given ans 變動
# print(s.checkInclusion(s1 = "ab", s2 = "accba"))
print(s.checkInclusion(s1 = "ab", s2 = "acdba"))

