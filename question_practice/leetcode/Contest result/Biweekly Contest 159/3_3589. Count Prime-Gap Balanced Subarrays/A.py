# 3589. Count Prime-Gap Balanced Subarrays
# https://leetcode.com/problems/count-prime-gap-balanced-subarrays/description/

from typing import List
from math import inf
from itertools import pairwise

# my v3 using given ans to optimize : 2095ms Beats75.31%
    # 1. not generate all facotors, only remove non-prime numbers
    # 2. use indx to filter removed number when tracing max and min
MAX = (5*(10**4))+1
prime = [True]*MAX
prime[0] = False
prime[1] = False
for i in range(2, int(MAX**(1/2)+1)):
    if not prime[i]:
        continue
    for j in range(i*i, MAX, i):
        prime[j] = False

from collections import Counter  
from heapq import heappop, heappush
class Trace_min_with_indx:
    def __init__(self):
        self.heap = []
        self.remove_count = Counter()
    
    def add(self, n, i):
        heappush(self.heap, (n,i))

    def min(self, i): # 剛好 i 會被保留
        while self.heap and self.heap[0][1] < i:
            heappop(self.heap)
        if self.heap:
            return self.heap[0][0]
        else :
            return 0

class Solution:
    def primeSubarray(self, nums: List[int], k: int) -> int:
        nums = list(n if prime[n] else 0 for n in nums)
        p_i = list(i for i, n in enumerate(nums) if n > 0)
        limit_l = []
        last_write = -1
        for p1, p2 in pairwise(p_i):
            limit_l += [p2]*(p1-last_write)
            last_write = p1

        l = 0
        ans = 0
        trace_max = Trace_min_with_indx()
        trace_min = Trace_min_with_indx()

        # sliding window
        r = -1
        ans = 0
        for l, r_limit in enumerate(limit_l):
            # 我希望 r 停在不行的那一格
            while r < len(nums) and (-trace_max.min(l) - trace_min.min(l)) <= k:
                r += 1
                if r == len(nums):
                    break
                r_n = nums[r]
                if r_n != 0:
                    trace_min.add(r_n, r)
                    trace_max.add(-r_n, r)
                    
            ans += r - r_limit
        return ans

# # my v1 (all factors + segment tree): 6131ms Beats10.45%
# MAX = ((10**4)*5)+1
# fac = [[] for _ in range(MAX)]
# for i in range(1, MAX):
#     for j in range(i, MAX, i):
#         fac[j].append(i)
# fac[1].append(1)
# fac[1].append(1)

# class SegTree:
#     def OP(self, val1, val2):
#         return [
#             max(val1[0], val2[0]),
#             min(val1[1], val2[1])
#         ]
    
#     def __init__(self, nums):
#         self.n = len(nums)
#         # init
#         self.tree = [None] * 2 * self.n
#         for i,n in zip(range(self.n, 2 * self.n) , nums):
#             if n == 0 :
#                 self.tree[i] = (0, inf) # [max, min]
#             else :
#                 self.tree[i] = (n, n)
#         for i in range(self.n-1, 0, -1):
#             # execute def
#             self.tree[i] = self.OP(self.tree[i<<1], self.tree[(i<<1)+1])

#     def query(self, left, right):
#         # include
#         left += self.n
#         right += self.n
#         res = (0, inf)
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 res = self.OP(res, self.tree[left])
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 res = self.OP(res, self.tree[right])
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return res

# class Solution:
#     def primeSubarray(self, nums: List[int], k: int) -> int:
#         nums = list(0 if len(fac[n]) > 2 else n for n in nums)
#         p_i = list(i for i, n in enumerate(nums) if n > 0)
#         limit_l = []
#         last_write = -1
#         for p1, p2 in pairwise(p_i):
#             limit_l += [p2]*(p1-last_write)
#             last_write = p1
        
#         # print(nums)
#         seg = SegTree(nums)

#         l = 0
#         ans = 0
#         def check(l,r):
#             max_q, min_q = seg.query(l,r)
#             if (max_q - min_q) > k :
#                 return False
#             return True

#         # sliding window
#         r = 0
#         ans = 0
#         for l, r_limit in enumerate(limit_l):
#             # r 會超出範圍
#             while r < len(nums) and check(l,r):
#                 r += 1
#             ans += r - r_limit
#         return ans

# from collections import Counter  
# from heapq import heappop, heappush
# class Trace_min:
#     def __init__(self):
#         self.heap = []
#         self.remove_count = Counter()
    
#     def add(self, n):
#         heappush(self.heap, n)

#     def remove(self, n):
#         self.remove_count[n] += 1

#     def min(self):
#         while self.heap and self.remove_count[self.heap[0]] > 0:
#             self.remove_count[heappop(self.heap)] -= 1
#         if self.heap:
#             return self.heap[0]
#         else :
#             return 0
    
# # my v2 (all factors + sliding window +using heap to trace max and min) : 3461ms Beats36.67%
# class Solution:
#     def primeSubarray(self, nums: List[int], k: int) -> int:
#         nums = list(0 if len(fac[n]) > 2 else n for n in nums)
#         p_i = list(i for i, n in enumerate(nums) if n > 0)
#         limit_l = []
#         last_write = -1
#         for p1, p2 in pairwise(p_i):
#             limit_l += [p2]*(p1-last_write)
#             last_write = p1

#         l = 0
#         ans = 0
#         trace_max = Trace_min()
#         trace_min = Trace_min()

#         # sliding window
#         r = -1
#         ans = 0
#         for l, r_limit in enumerate(limit_l):
#             # 我希望 r 停在不行的那一格
#             while r < len(nums) and (-trace_max.min() - trace_min.min()) <= k:
#                 r += 1
#                 if r == len(nums):
#                     break
#                 r_n = nums[r]
#                 if r_n != 0:
#                     trace_min.add(r_n)
#                     trace_max.add(-r_n)
                    
#             ans += r - r_limit
#             l_n = nums[l]
#             if l_n != 0:
#                 trace_min.remove(nums[l])
#                 trace_max.remove(-nums[l])
#         return ans
            

s = Solution()
print("ans :",s.primeSubarray(nums = [1,2,3], k = 1)) # 2
print("ans :",s.primeSubarray(nums = [2,3,5,7], k = 3)) # 4
# print("ans :",s.primeSubarray()) # 



