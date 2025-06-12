# 440. K-th Smallest in Lexicographical Order
# https://leetcode.com/problems/k-th-smallest-in-lexicographical-order

from typing import List
from math import inf
from functools import cache
import math

# # my v1 (passing in int)
# # 0ms Beats100.00%, 18.13MB Beats18.91%
# class Solution:
#     def findKthNumber(self, n: int, k: int) -> int:
#         str_n = str(n)
        
#         init_pos = int(math.log(n,10)) + 1
#         # print("init_pos",init_pos)

#         after_n = [None] + list(range(10))
#         # print("after_n",after_n)

#         @cache
#         def cal_all_pos(now_p):
#             if now_p == 0 :
#                 return 0
#             num_s = "1"*now_p
#             return int(num_s)
#         def find_k(now_n,now_p,k):
#             for i in range(1,10) if now_p == init_pos else after_n :
#                 if i == None :
#                     if k == 1 :
#                         return now_n
#                     else :
#                         k -= 1
#                     continue

#                 # cal all poss
#                 now_f = now_n*10+i
#                 str_now_f = str(now_f)
#                 front_n = str_n[:len(str_now_f)]
#                 if front_n == str_now_f :
#                     #limited = 少一位數的全部可能    + n 以下的數字
#                     all_comb = cal_all_pos(now_p-1) + (n-now_f*(10**(now_p-1))+1)
#                 elif front_n < str_now_f :
#                     all_comb = cal_all_pos(now_p-1)
#                 else :
#                     all_comb = cal_all_pos(now_p)
#                 if all_comb >= k :
#                     return find_k(now_f,now_p-1,k)
#                 else :
#                     k -= all_comb
#             raise Exception
#         return find_k(0,init_pos,k)

# my v2 (passing in str)
# 0ms Beats100.00%, 17.76MB Beats64.68%
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        str_n = str(n)
        
        init_pos = int(math.log(n,10)) + 1
        # print("init_pos",init_pos)

        after_n = [None] + list(str(i) for i in range(10))
        # print("after_n",after_n)

        @cache
        def cal_all_pos(now_p):
            if now_p == 0 :
                return 0
            num_s = "1"*now_p
            return int(num_s)
        def find_k(now_n,now_p,k):
            for i in map(str,range(1,10)) if now_p == init_pos else after_n :
                if i == None :
                    k -= 1
                    if k == 0 :
                        return now_n
                    continue

                # cal all poss
                new_f = now_n+i
                front_n = str_n[:len(new_f)]
                if front_n == new_f :
                    #limited = 少一位數的全部可能    + n 以下的數字
                    all_comb = cal_all_pos(now_p-1) + (n-(int(new_f)*(10**(now_p-1)))+1)
                elif front_n < new_f :
                    all_comb = cal_all_pos(now_p-1)
                else :
                    all_comb = cal_all_pos(now_p)
                if all_comb >= k :
                    return find_k(new_f,now_p-1,k)
                else :
                    k -= all_comb
            raise Exception
        return int( find_k("", init_pos, k) )

# given ans
class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        ans = 1
        i = 1
        while i < k:
            gap = self._getGap(ans, ans + 1, n)
            if i + gap <= k:
                i += gap
                ans += 1
            else:
                i += 1
                ans *= 10

        return ans

    def _getGap(self, a: int, b: int, n: int) -> int:
        gap = 0
        while a <= n:
            gap += min(n + 1, b) - a
            a *= 10
            b *= 10
        return gap

s = Solution()
print("ans :",s.findKthNumber(n = 13, k = 2)) # 10
print("ans :",s.findKthNumber(n = 1, k = 1)) # 1
print("ans :",s.findKthNumber(n = 2, k = 2)) # 2
print("ans :",s.findKthNumber(n = 10, k = 3)) # 2
print("ans :",s.findKthNumber(n = 100, k = 90)) # 9
print("ans :",s.findKthNumber(n = 100, k = 100)) # 99



