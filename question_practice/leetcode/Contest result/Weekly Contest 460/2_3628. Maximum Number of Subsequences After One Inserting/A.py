# 3628. Maximum Number of Subsequences After One Inserting
# https://leetcode.com/problems/maximum-number-of-subsequences-after-one-inserting/description/

from typing import List
from math import inf
from collections import Counter

# my opt 731ms Beats-%
class Solution:
    def numOfSubsequences(self, s: str) -> int:
        def cal_comb(s):
            ret = 0
            cnt = Counter()
            cnt_LC = 0
            for c in s :
                if c == "C" :
                    cnt_LC += cnt["L"]
                if c == "T" :
                    ret += cnt_LC
                cnt[c] += 1
            return ret, cnt_LC
        
        # case +L 一定是放在最前面
        case_L = cal_comb("L"+s)[0]

        # normal
        normal, cnt_LC = cal_comb(s)

        # case +C 會放在 cnt_L * cnt_T 最大的位置
        total_cnt_T = s.count("T")
        case_C = 0
        cnt = Counter()
        for c in s :
            cnt[c] += 1
            if (new_add := cnt["L"]*(total_cnt_T - cnt["T"])) > case_C :
                case_C = new_add
        case_C += normal

        # case +T 一定是放在最後面
        case_T = cnt_LC + normal

        # print(case_L, case_C, case_T)
        return max(case_L, case_C, case_T)
    
# # my 915ms Beats-%
#     # can be optimized : since there are many similar calculation, but in contest I don't have time
#         # EX: Keep the result of cnt_LC from cal_comb(s), then cal_comb(s+"T") can be calculate immediately
# class Solution:
#     def numOfSubsequences(self, s: str) -> int:
#         def cal_comb(s):
#             ret = 0
#             cnt = Counter()
#             cnt_LC = 0
#             for c in s :
#                 if c == "C" :
#                     cnt_LC += cnt["L"]
#                 if c == "T" :
#                     ret += cnt_LC
#                 cnt[c] += 1
#             return ret
        
#         # case +L 一定是放在最前面
#         case_L = cal_comb("L"+s)

#         # case +C 會放在 cnt_L * cnt_T 最大的位置
#         case_C = cal_comb(s)
#         total_cnt_T = s.count("T")
#         max_add = 0
#         cnt = Counter()
#         for c in s :
#             cnt[c] += 1
#             if (new_add := cnt["L"]*(total_cnt_T - cnt["T"])) > max_add :
#                 max_add = new_add
#         case_C += max_add

#         # case +T 一定是放在最後面
#         case_T = cal_comb(s+"T")

#         # print(case_L, case_C, case_T)
#         return max(case_L, case_C, case_T) 

s = Solution()
print("ans :",s.numOfSubsequences("LMCT")) # 2
print("ans :",s.numOfSubsequences("LCCT")) # 4
print("ans :",s.numOfSubsequences("L")) # 0
print("ans :",s.numOfSubsequences("LC")) # 1
print("ans :",s.numOfSubsequences("LCTKLCLT")) # 7

