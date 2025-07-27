# 3480. Maximize Subarrays After Removing One Conflicting Pair
# https://leetcode.com/problems/maximize-subarrays-after-removing-one-conflicting-pair

from typing import List
from math import inf

# inspire by given ans : 503ms Beats93.69%
class Solution:
    def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
        # 1. 先計算 全部沒有 conflictingPairs 的組合有多少個
        # 2. 計算每一條路線 若移除可以新增幾種組合 
        # 統計每個點 前面不能連到的點
        max_right = [[] for _ in range(n+1)]
        for st, en in conflictingPairs :
            if st > en :
                st, en = en, st
            max_right[en].append(st)
        
        # max_right[i][0] 就是最近一個不能連到的點
        # max_right[i][1] 就是若取消這個conflictingPairs 最近一個不能連到的點
        for i in range(n+1) :
            max_right[i].sort(reverse=True)

        remove_add = [0]*(n+1)

        max_r = 0
        max_r2 = 0
        ans = 0
        for now_i, max_r_l in enumerate(max_right[1:], 1):
            if max_r_l :
                new_max_r = max_r_l[0]
                if new_max_r > max_r :
                    max_r2 = max_r
                    max_r = new_max_r
                elif new_max_r > max_r2 :
                    max_r2 = new_max_r
            if len(max_r_l) >= 2 :
                new_max_r = max_r_l[1]
                if new_max_r > max_r2 :
                    max_r2 = new_max_r
            ans += (now_i - max_r)
            remove_add[max_r] += (max_r - max_r2)
        
        # print(ans, remove_add)
        return ans + max(remove_add)

# my 
    # fail : 卡在如何使用 O(n) 計算 若移除可以新增幾種組合
        # 相乘是錯的， 應該是每個數字可新增組合的總和 
# class Solution:
#     def maxSubarrays(self, n: int, conflictingPairs: List[List[int]]) -> int:
#         conflictingPairs = list( (st, en) if st < en else (en, st) for st, en in conflictingPairs)

#         # 1. 先計算 全部沒有 conflictingPairs 的組合有多少個
#         # 找出每個點 可以連接最遠的點
#         end_i = n+1
#         min_left = [end_i]*(n+1)
#         max_right = [0]*(n+1)
#         for st, en in conflictingPairs :
#             if en < min_left[st] :
#                 min_left[st] = en
#             if st > max_right[en] :
#                 max_right[en] = st
        
#         min_l = end_i
#         for i in range(len(min_left)-1,-1,-1) :
#             if min_l > min_left[i] :
#                 min_l = min_left[i]
#             else :
#                 min_left[i] = min_l
#         print(min_left)
#         max_r = 0
#         for i in range(len(max_right)):
#             if max_r < max_right[i] :
#                 max_r = max_right[i]
#             else :
#                 max_right[i] = max_r
#         print(max_right)
        
#         # 再根據最遠可到的點 計算有幾種可能
#         print(list((en-st) for st, en in enumerate(min_left[1:], 1)))
#         combs = sum((en-st) for st, en in enumerate(min_left[1:], 1))
#         print(combs)

#         # 2. 計算每一條路線 若移除可以新增幾種組合
#         # [st, en] 分別向兩邊擴散 
#         max_mul = 0
#         _r,_l = -1,-1
#         for st, en in conflictingPairs :
#             l = (st-max_right[st])
#             r = (min_left[en]-en)
#             if (new_mul := (l*r)) > max_mul :
#                 max_mul = new_mul
#                 _r,_l = r,l
#         print(_r,_l)
#         print(combs , max_mul)
#         return combs + max_mul -1


s = Solution()
print("ans :",s.maxSubarrays(n = 4, conflictingPairs = [[2,3],[1,4]])) # 9
print("ans :",s.maxSubarrays(n = 5, conflictingPairs = [[1,2],[2,5],[3,5]])) # 12
# print("ans :",s.maxSubarrays()) # 



