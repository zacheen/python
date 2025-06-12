# 3510. Minimum Pair Removal to Sort Array II
# https://leetcode.com/problems/minimum-pair-removal-to-sort-array-ii/description/

from typing import List
from math import inf
from itertools import pairwise
from bisect import bisect_left
from sortedcontainers import SortedList, SortedSet
from heapq import heappop, heappush, heapify

# my, adjust by given ans (heap) : 1894ms Beats95.67%
    # when pop, check its validation
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        if len(nums) <= 1 :
            return 0
        
        # 目前總共 inc_cou 數量
        inc_cou = sum(n1 <= n2 for n1,n2 in pairwise(nums))

        # 用來記錄現在最小的和 以及其位置(在rem_indx中的位置)
        # [ (sum, front_pos), ...
        sum_ord = list((n1+n2, fro_i) for fro_i, (n1,n2) in enumerate(pairwise(nums)))
        heapify(sum_ord)

        front_rel = list(range(-1,len(nums)-1)) + [-1]
        back_rel = list(range(1,len(nums))) + [-1,-1]

        ans = 0
        need_inc_cou = len(nums)-1
        while need_inc_cou-ans > inc_cou :
            # pop the smallest sum
            min_sum, mer_l_i = heappop(sum_ord)

            # check validation
            mer_l_n = nums[mer_l_i]
            mer_r_i = back_rel[mer_l_i]
            mer_r_n = nums[mer_r_i]
            if mer_l_n + mer_r_n != min_sum :
                continue

            # update merge (already pop)
            if mer_l_n <= mer_r_n :
                inc_cou -= 1

            # update front
            if (prev_i:=front_rel[mer_l_i]) >= 0: # 前面還有項目
                # del old
                pre_n = nums[prev_i]
                if pre_n <= mer_l_n :
                    inc_cou -= 1
                # new nums
                if pre_n <= min_sum :
                    inc_cou += 1
                heappush(sum_ord, (pre_n+min_sum, prev_i) )

            # update back
            if (next_i:=back_rel[mer_r_i]) >= 0 : # 合併的後面還有項目
                next_n = nums[next_i]
                # del old
                if mer_r_n <= next_n :
                    inc_cou -= 1
                # new nums
                if min_sum <= next_n :
                    inc_cou += 1
                heappush(sum_ord, (min_sum+next_n, mer_l_i) )

            # update nums
            nums[mer_l_i] = min_sum
            nums[mer_r_i] = inf
            front_rel[next_i] = mer_l_i
            back_rel[mer_l_i] = next_i
            ans += 1

        return ans

# # my, adjust by given ans (indicate) : 3342ms Beats59.61%
#     # similar to link list
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         if len(nums) <= 1 :
#             return 0
        
#         # 紀錄現在已經有幾個項目合乎遞增規則
#         inc_cou = sum(1 for n1,n2 in pairwise(nums) if n1 <= n2)

#         # 用來記錄現在最小的和 以及其位置(在rem_indx中的位置)
#         # [ (sum, front_pos), ...
#         sum_ord = SortedList((n1+n2, fro_i) for fro_i, (n1,n2) in enumerate(pairwise(nums)))
#         # print(sum_ord)

#         front_rel = list(range(-1,len(nums)))
#         back_rel = list(range(1,len(nums)+2))

#         while sum_ord :
#             if inc_cou == len(sum_ord) :
#                 return len(nums) - len(sum_ord) - 1
        
#             # pop the smallest sum
#             min_sum, mer_l_i = sum_ord.pop(0)

#             # indx pos 
#             mer_l_n = nums[mer_l_i]

#             # update merge (already pop)
#             mer_r_i = back_rel[mer_l_i]
#             mer_r_n = nums[mer_r_i]
#             if mer_l_n <= mer_r_n :
#                 inc_cou -= 1

#             # update front
#             if (prev_i:=front_rel[mer_l_i]) >= 0: # 前面還有項目
#                 # del old
#                 pre_n = nums[prev_i]
#                 if pre_n <= mer_l_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (pre_n+mer_l_n, prev_i) )
#                 # new nums
#                 if pre_n <= min_sum :
#                     inc_cou += 1
#                 sum_ord.add( (pre_n+min_sum, prev_i) )

#             # update back
#             if (next_i:=back_rel[mer_r_i]) < len(nums) : # 合併的後面還有項目
#                 next_n = nums[next_i]
#                 # del old
#                 if mer_r_n <= next_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (mer_r_n+next_n, mer_r_i) )
#                 # new nums
#                 if min_sum <= next_n :
#                     inc_cou += 1
#                 sum_ord.add( (min_sum+next_n, mer_l_i) )

#             # update rem_indx
#             nums[mer_l_i] = min_sum
#             # nums[mer_r_i] = None
#             front_rel[next_i] = mer_l_i
#             back_rel[mer_l_i] = next_i

#         return len(nums)-1

# # my, adjust by given ans (UF) : 4154ms Beats52.88%
# class UF_no_init:
#     def __init__(self):
#         self.id = {}                # <適用各種type> 多的

#     def union(self, u, v):
#         i = self.find(u)
#         j = self.find(v)
#         if i == j:
#             return
#         self.id[i] = j

#     def find(self, up):
#         while up in self.id and up != (deep:=self.id[up]):
#             self.id[up] = up = self.id[deep] if deep in self.id else deep
#         return up
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         if len(nums) <= 1 :
#             return 0
        
#         # 紀錄現在已經有幾個項目合乎遞增規則
#         inc_cou = sum(1 for n1,n2 in pairwise(nums) if n1 <= n2)

#         # 用來記錄現在最小的和 以及其位置(在rem_indx中的位置)
#         # [ (sum, front_pos), ...
#         sum_ord = SortedList((n1+n2, fro_i) for fro_i, (n1,n2) in enumerate(pairwise(nums)))
#         # print(sum_ord)

#         front_rel = UF_no_init()
#         back_rel = UF_no_init()

#         while sum_ord :
#             if inc_cou == len(sum_ord) :
#                 return len(nums) - len(sum_ord) - 1
        
#             # pop the smallest sum
#             min_sum, mer_l_i = sum_ord.pop(0)

#             # indx pos 
#             mer_l_n = nums[mer_l_i]

#             # update merge (already pop)
#             mer_r_i = back_rel.find(mer_l_i+1)
#             mer_r_n = nums[mer_r_i]
#             if mer_l_n <= mer_r_n :
#                 inc_cou -= 1

#             # update front
#             if (prev_i:=front_rel.find(mer_l_i-1)) >= 0: # 前面還有項目
#                 # del old
#                 pre_n = nums[prev_i]
#                 if pre_n <= mer_l_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (pre_n+mer_l_n, prev_i) )
#                 # new nums
#                 if pre_n <= min_sum :
#                     inc_cou += 1
#                 sum_ord.add( (pre_n+min_sum, prev_i) )

#             # update back
#             if (next_i:=back_rel.find(mer_r_i+1)) < len(nums) : # 合併的後面還有項目
#                 next_n = nums[next_i]
#                 # del old
#                 if mer_r_n <= next_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (mer_r_n+next_n, mer_r_i) )
#                 # new nums
#                 if min_sum <= next_n :
#                     inc_cou += 1
#                 sum_ord.add( (min_sum+next_n, mer_l_i) )

#             # update rem_indx
#             nums[mer_l_i] = min_sum
#             nums[mer_r_i] = None
#             front_rel.union(mer_r_i, mer_l_i)
#             back_rel.union(mer_r_i, next_i)

#         return len(nums)-1

# my Time Limit Exceeded
# class Solution:
#     def minimumPairRemoval(self, nums: List[int]) -> int:
#         if len(nums) <= 1 :
#             return 0
        
#         # 紀錄現在已經有幾個項目合乎遞增規則
#         inc_cou = sum(1 for n1,n2 in pairwise(nums) if n1 <= n2)
        
#         # 紀錄現在剩下的 indx (因為每次合併都會少掉幾個) (所以這是為了找上一個跟下一個項目是誰)
#         rem_indx = SortedSet(range(len(nums)))

#         # 用來記錄現在最小的和 以及其位置(在rem_indx中的位置)
#         # [ (sum, front_pos), ...
#         sum_ord = SortedList((n1+n2, fro_i) for fro_i, (n1,n2) in enumerate(pairwise(nums)))
#         # print(sum_ord)

#         while sum_ord :
#             if inc_cou == len(rem_indx)-1 :
#                 return len(nums) - len(rem_indx)
        
#             # pop the smallest sum
#             min_sum, min_i = sum_ord.pop(0)

#             # indx pos
#             rem_mer_l_i = bisect_left(rem_indx, min_i) 
#             mer_l_i = rem_indx[rem_mer_l_i]
#             mer_l_n = nums[mer_l_i]

#             # update merge (already pop)
#             rem_mer_r_i = rem_mer_l_i+1
#             mer_r_i = rem_indx[rem_mer_r_i]
#             mer_r_n = nums[mer_r_i]
#             if mer_l_n <= mer_r_n :
#                 inc_cou -= 1

#             # update front
#             if rem_mer_l_i > 0 : # 前面還有項目
#                 rem_prev_i = rem_mer_l_i-1
#                 prev_i = rem_indx[rem_prev_i]
#                 # del old
#                 pre_n = nums[prev_i]
#                 if pre_n <= mer_l_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (pre_n+mer_l_n, prev_i) )
#                 # new nums
#                 if pre_n <= min_sum :
#                     inc_cou += 1
#                 sum_ord.add( (pre_n+min_sum, prev_i) )

#             # update back
#             rem_next_i = rem_mer_r_i+1
#             if rem_next_i < len(rem_indx) : # 合併的後面還有項目
#                 next_n = nums[rem_indx[rem_next_i]]
#                 # del old
#                 if mer_r_n <= next_n :
#                     inc_cou -= 1
#                 sum_ord.remove( (mer_r_n+next_n, mer_r_i) )
#                 # new nums
#                 if min_sum <= next_n :
#                     inc_cou += 1
#                 sum_ord.add( (min_sum+next_n, mer_l_i) )

#             # update rem_indx
#             nums[mer_l_i] = min_sum
#             # nums[mer_r_i] = None
#             rem_indx.remove(mer_r_i)

#         return len(nums)-1

s = Solution()
print("ans :",s.minimumPairRemoval([5,2,3,1])) # 2 : > [5,2,4] > [5,6]
print("ans :",s.minimumPairRemoval([1,2,2])) # 0
print("ans :",s.minimumPairRemoval([2,2,-1,3,-2,2,1,1,1,0,-1])) # 9
print("ans :",s.minimumPairRemoval([-2,1,2,-1,-1,-2,-2,-1,-1,1,1])) # 10
print("ans :",s.minimumPairRemoval([1,1,4,4,2,-4,-1])) # 



