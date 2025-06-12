# 3505. Minimum Operations to Make Elements Within K Subarrays Equal
# https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/description/

from typing import List
from math import inf
from collections import defaultdict
from heapq import heappushpop, heappush
from functools import cache
from sortedcontainers import SortedList

# my optimized by given ans with easier index : 2724ms Beats94.07%
class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        op_num_st_i = []
        # med_i = x//2
        med_end = (x+1)//2
        l = SortedList(nums[:x])
        fro_l = SortedList(l[:med_end])
        bac_l = SortedList(l[med_end:])
        odd_f = x%2 == 1
        # sum = 後半部 - 前半部 (不包含 med,) 
        pre_sum = sum(bac_l) - sum(fro_l)
        if odd_f :
            op_num_st_i.append(pre_sum + fro_l[-1])
        else :
            op_num_st_i.append(pre_sum)
        # fro_l 的數量一定 1. 等於bac_l 2. 多bac_l一個
            # 所以 fro_l[-1] 一定是 median
        def balance():
            nonlocal fro_l, bac_l, pre_sum
            if len(fro_l) > len(bac_l) + 1 :
                move_num = fro_l.pop(-1)
                bac_l.add(move_num)
                pre_sum += move_num*2
            elif len(bac_l) > len(fro_l):
                move_num = bac_l.pop(0)
                fro_l.add(move_num)
                pre_sum -= move_num*2

        for rem_i, add_i in zip(range(0,len(nums)), range(x,len(nums))) :
            # using pre_sum to cal new sum 
            add_n = nums[add_i]
            rem_n = nums[rem_i]
            
            if not fro_l or add_n <= fro_l[-1] :
                fro_l.add(add_n)
                pre_sum -= add_n
            else :
                bac_l.add(add_n)
                pre_sum += add_n

            if rem_n <= fro_l[-1] :
                fro_l.remove(rem_n)
                pre_sum += rem_n
            else :
                bac_l.remove(rem_n)
                pre_sum -= rem_n
            
            balance()
            if odd_f :
                op_num_st_i.append(pre_sum + fro_l[-1])
            else :
                op_num_st_i.append(pre_sum)

        # dp to find the min operation
        # 雖然不知道為什麼 但這裡一定要用 for，不能用 recursive (會 Memory Limit Exceeded)
        init = [0]+[inf for _ in range(k)]
        dp = [init for _ in range(x)]
        for now_i in range(len(op_num_st_i)) :
            # dont take
            new_dp = dp[-1].copy()
            for each_k in range(1,k+1) :
                # take
                if (new_c := dp[-x][each_k-1] + op_num_st_i[now_i]) < new_dp[each_k] :
                    new_dp[each_k] = new_c
            dp.append(new_dp)
        return dp[-1][k]   

        
# # my 2714ms Beats96.25%
# class Solution:
#     def minOperations(self, nums: List[int], x: int, k: int) -> int:
#         # calcualte the op num to let [st:st+x] the same
#         op_num_st_i = []
#         mid_i = x//2
#         l = SortedList(nums[:x])
#         # sum = 後半部 - 前半部
#         odd_f = x%2 == 1
#         if odd_f :
#             fro_l = SortedList(l[:mid_i])
#             bac_l = SortedList(l[mid_i+1:])
#             pre_med = l[mid_i]
#         else :
#             fro_l = SortedList(l[:mid_i])
#             bac_l = SortedList(l[mid_i:])
#         del(l)
#         pre_sum = sum(bac_l) - sum(fro_l)
#         op_num_st_i.append(pre_sum)
#         for rem_i, add_i in zip(range(0,len(nums)), range(x,len(nums))) :
#             # using pre_med and pre_sum to cal new sum 
#             new_sum = pre_sum
#             rem_n = nums[rem_i]
#             add_n = nums[add_i]

#             # 加入新的 add_n
#             if (odd_f and add_n >= pre_med) or (not odd_f and bac_l and add_n >= bac_l[0]) :
#                 bac_l.add(add_n)
#                 new_sum += add_n
#             else :
#                 fro_l.add(add_n)
#                 new_sum -= add_n

#             # 移除舊的 rem_n
#             if bac_l and rem_n >= bac_l[0] :
#                 bac_l.remove(rem_n)
#                 new_sum -= rem_n
#             elif fro_l and rem_n <= fro_l[-1] :
#                 fro_l.remove(rem_n)
#                 new_sum += rem_n
#             else : # rem_n == pre_med
#                 # 先從 bac_l pop 一個頂替
#                 if bac_l :
#                     pre_med = bac_l.pop(0)
#                     new_sum -= pre_med
#                 else :
#                     pre_med = fro_l.pop(-1)
#                     new_sum += pre_med
                
#             if len(bac_l) > len(fro_l) :
#                 if odd_f :
#                     fro_l.add(pre_med)
#                     new_sum -= pre_med
#                     pre_med = bac_l.pop(0)
#                     new_sum -= pre_med
#                 else :
#                     move_num = bac_l.pop(0)
#                     fro_l.add(move_num)
#                     new_sum -= move_num*2
#             elif len(fro_l) > len(bac_l) :
#                 if odd_f :
#                     bac_l.add(pre_med)
#                     new_sum += pre_med
#                     pre_med = fro_l.pop(-1)
#                     new_sum += pre_med
#                 else :
#                     move_num = fro_l.pop(-1)
#                     bac_l.add(move_num)
#                     new_sum += move_num*2

#             op_num_st_i.append(new_sum)
#             pre_sum = new_sum
        
#         # dp to find the min operation
#         # 雖然不知道為什麼 但這裡一定要用 for，不能用 recursive (會 Memory Limit Exceeded)
#         init = [0]+[inf for _ in range(k)]
#         dp = [init for _ in range(x)]
#         for now_i in range(len(op_num_st_i)) :
#             # dont take
#             new_dp = dp[-1].copy()
#             for each_k in range(1,k+1) :
#                 # take
#                 if (new_c := dp[-x][each_k-1] + op_num_st_i[now_i]) < new_dp[each_k] :
#                     new_dp[each_k] = new_c
#             dp.append(new_dp)
#         return dp[-1][k]
            
# # my Time Limit Exceeded : I thought maximum of x is also 15
# class Solution:
#     def minOperations(self, nums: List[int], x: int, k: int) -> int:
#         # calcualte the op num to let [st:st+x] the same
#         op_num_st_i = []
#         def cal_op(st, med):
#             return sum(abs(n-med) for n in nums[st:st+x])
#         for st, en in zip(range(0,len(nums)), range(x,len(nums)+1)) :
#             l = nums[st:en]
#             l.sort()
#             med = l[len(l)//2]
#             op_num_st_i.append(cal_op(st, med))
        
#         # dp to find the min operation
#         @cache
#         def dp(now_i, rem_k):
#             if now_i >= len(op_num_st_i) :
#                 if rem_k == 0 :
#                     return 0
#                 else :
#                     return inf
#             # take
#             ret = dp(now_i+x, rem_k-1) + op_num_st_i[now_i]
#             # dont take
#             ret = min(ret, dp(now_i+1, rem_k))
#             return ret
#         return dp(0, k)
        

# given ans


s = Solution()
print("ans :",s.minOperations(nums = [5,-2,1,3,7,3,6,4,-1], x = 3, k = 2)) # 8
print("ans :",s.minOperations(nums = [9,-2,-2,-2,1,5], x = 2, k = 2)) # 3
print("ans :",s.minOperations(nums = [17,-1], x = 1, k = 2)) # 0
print("ans :",s.minOperations(nums = [0,18,-13], x = 2, k = 1)) # 18



