# 3501. Maximize Active Section with Trade II
# https://leetcode.com/problems/maximize-active-section-with-trade-ii/description/

from typing import List
from math import inf
from itertools import pairwise
from bisect import bisect_left, bisect_right

# given ans
class SparseTable:
    def __init__(self, a):
        n = len(a) - 1
        m = n.bit_length()
        st = [[r1 - l1 + r2 - l2] + [0] * (m - 1) for (l1, r1), (l2, r2) in pairwise(a)]
        for j in range(1, m):
            for i in range(n - (1 << j) + 1):
                st[i][j] = max(st[i][j - 1], st[i + (1 << (j - 1))][j - 1])
        self.st = st

    # 查询区间最大值，[l,r) 左闭右开
    def query(self, l: int, r: int) -> int:
        if l >= r:
            return 0
        k = (r - l).bit_length() - 1
        return max(self.st[l][k], self.st[r - (1 << k)][k])

class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        total1 = 0
        # 统计连续 0 段对应的区间（左闭右开）
        a = [(-1, -1)]  # 哨兵
        start = 0
        for i, b in enumerate(s):
            if i == n - 1 or b != s[i + 1]:
                if b == '1':
                    total1 += i - start + 1
                else:
                    a.append((start, i + 1))  # 左闭右开
                start = i + 1
        a.append((n + 1, n + 1))  # 哨兵

        def merge(x: int, y: int) -> int:
            return x + y if x > 0 and y > 0 else 0

        st = SparseTable(a)
        ans = []
        for ql, qr in queries:
            qr += 1  # 左闭右开
            i = bisect_left(a, ql, key=lambda p: p[0])
            j = bisect_right(a, qr, key=lambda p: p[1]) - 1
            mx = 0
            if i <= j:  # [ql,qr) 中有完整的区间
                mx = max(
                    st.query(i, j),  # 相邻完整区间的长度之和的最大值
                    merge(a[i - 1][1] - ql, a[i][1] - a[i][0]),  # 残缺区间 i-1 + 完整区间 i
                    merge(qr - a[j + 1][0], a[j][1] - a[j][0]),  # 残缺区间 j+1 + 完整区间 j
                )
            elif i == j + 1:  # [ql,qr) 中有两个相邻的残缺区间
                mx = merge(a[i - 1][1] - ql, qr - a[j + 1][0])  # 残缺区间 i-1 + 残缺区间 j+1
            ans.append(total1 + mx)
        return ans

# my 
    # I dont understant why 
    #     Query [2, 3] → Substring "00" → Augmented to "1001"
    #     Because there is no block of '1's surrounded by '0's, no valid trade is possible. 
    #     The maximum number of active sections is 1. (instead of 0)
# class SegTree_max_zero:
#     def __init__(self, nums):
#         self.n = len(nums)
#         # init
#         self.tree = [0] * 2 * self.n
#         for i,n in zip(range(self.n, 2 * self.n) , nums):
#             self.tree[i] = n
#         for i in range(self.n-1, 0, -1):
#             # execute def
#             self.tree[i] = max(self.tree[2*i], self.tree[2*i+1])

#     def update(self, index, diff):
#         index += self.n
#         self.tree[index] -= diff
#         while index > 1:
#             # update node
#             self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
#             index >>= 1

#     def query(self, left, right):
#         # include
#         left += self.n
#         right += self.n
#         res = 0
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 res = max(res,self.tree[left])
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 res = max(res,self.tree[right])
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return res
    
# class SegTree_sum_one:
#     def __init__(self, nums):
#         self.n = len(nums)
#         # init
#         self.tree = [0] * 2 * self.n
#         for i,n in zip(range(self.n, 2 * self.n) , nums):
#             self.tree[i] = n
#         for i in range(self.n-1, 0, -1):
#             # execute def
#             self.tree[i] = self.tree[2*i] + self.tree[2*i+1]

#     def update(self, index, diff):
#         index += self.n
#         self.tree[index] -= diff
#         while index > 1:
#             # update node
#             self.tree[index>>1] = self.tree[index] + self.tree[index^1]
#             index >>= 1

#     def query(self, left, right):
#         # include
#         left += self.n
#         right += self.n
#         res = 0
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 res += self.tree[left]
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 res += self.tree[right]
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return res

# class Solution:
#     def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
#         sh_cou = []
#         cou = 1
#         pre_c = "1"
#         st_i = 0
#         for now_i, c in enumerate(s) :
#             if pre_c == c :
#                 cou += 1
#             else :
#                 sh_cou.append((cou,st_i,now_i))
#                 pre_c = c
#                 cou = 1
#                 st_i = now_i+1
#         if pre_c == "1" :
#             sh_cou.append((cou+1, st_i, now_i+2))
#         else :
#             sh_cou.append((cou, st_i, now_i+1))
#             sh_cou.append((1, now_i+2, now_i+2))

#         only_zero = [cou for i, cou in enumerate(sh_cou) if i%2 == 1]
#         # only_zero.append((0,inf,inf))
#         pass_in_zero = [cou1[0]+cou2[0] for cou1,cou2 in pairwise(only_zero)]
#         seg_zero = SegTree_max_zero(pass_in_zero)

#         only_one = [cou for i, cou in enumerate(sh_cou) if i%2 == 0]
#         # only_zero.append((0,inf,inf))
#         pass_in_one = [item[0] for item in only_one]
#         seg_one = SegTree_sum_one(pass_in_one)

#         ans = []
#         for q_st, q_en in queries :
#             sh_q_st = q_st+1
#             sh_q_en = q_en+1

#             # 不夠轉換 (直接計算 1 有幾個)
#             if sh_q_st >= only_one[-2][1] :
#                 ze_l_i = max(sh_q_st, only_zero[-1][1])
#                 ze_r_i = max(sh_q_en, only_zero[-1][0])
#                 if ze_r_i <= ze_l_i :
#                     ans.append(sh_q_en-sh_q_st+1)
#                 else :
#                     ans.append(sh_q_en-sh_q_st+1 - (ze_r_i-ze_l_i+1))
#                 continue
#             if sh_q_en <= only_one[1][2] :
#                 ans.append(-1)
#                 continue
            
#             zero_diff_1 = 0
#             zero_diff_2 = 0
#             one_diff_1 = 0
#             one_diff_2 = 0
            
#             # 找到對應區間                  q_st+1 因為要加上 extend 的 1
#             ins_i = bisect_left(only_zero, sh_q_st, key= lambda x : x[1])
#             if s[q_st] == '0' :
#                 # 這是在 0 之內
#                 ze_info = only_zero[ins_i]
#                 zero_diff_1 = sh_q_st-ze_info[1]
#                 seg_zero.update(ins_i, zero_diff_1)
#             else :
#                 # 在 1 之內
#                 one_info = only_one[ins_i]
#                 one_diff_1 = sh_q_st-one_info[1]
#                 seg_one.update(ins_i, one_diff_1)
            
#             ins_i_2 = bisect_left(only_zero, sh_q_en, key= lambda x : x[2])
#             if s[q_en] == '0' :
#                 # 這是在 0 之內
#                 ze_info = only_zero[ins_i_2]
#                 zero_diff_2 = ze_info[2]-sh_q_en
#                 seg_zero.update(ins_i_2-1, zero_diff_2)
#             else :
#                 # 在 1 之內
#                 one_info = only_one[ins_i_2]
#                 one_diff_2 = one_info[2]-sh_q_en
#                 seg_one.update(ins_i_2, one_diff_2)
            
#             max_zero_c = seg_zero.query(ins_i, ins_i_2-1)
#             if s[q_en] == '0' :
#                 period_one = seg_one.query(ins_i, ins_i_2-1)
#             else :
#                 period_one = seg_one.query(ins_i, ins_i_2)
#             ans.append(period_one + max_zero_c)

#             # 更新回來
#             if zero_diff_1 :
#                 seg_zero.update(ins_i, -zero_diff_1)
#             if one_diff_1 :
#                 seg_one.update(ins_i, -one_diff_1)
#             if zero_diff_2 :
#                 seg_zero.update(ins_i_2-1, -zero_diff_2)
#             if one_diff_2 :
#                 seg_one.update(ins_i_2, -one_diff_2)
#         return ans
        

s = Solution()
print("ans :",s.maxActiveSectionsAfterTrade(s = "0100", queries = [[0,3],[0,2],[1,3],[2,3]])) # 4,3,1,1
# print("ans :",s.maxActiveSectionsAfterTrade(s = "01001", queries = [[0,3],[0,2],[1,3],[2,3]])) # 4,3,1,1
print("ans :",s.maxActiveSectionsAfterTrade(s = "1000100", queries = [[1,5],[0,6],[0,4]])) # 6,7,2





