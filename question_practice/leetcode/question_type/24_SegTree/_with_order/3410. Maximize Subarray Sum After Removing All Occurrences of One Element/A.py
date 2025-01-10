# 3410. Maximize Subarray Sum After Removing All Occurrences of One Element
# https://leetcode.com/problems/maximize-subarray-sum-after-removing-all-occurrences-of-one-element/description/

from typing import List
import functools

# given ans : DP with Kadane
# 271ms Beats77.19%
from collections import Counter
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        res = nums[0]
        now_sum = 0 # 到現在這個數字的總和
        min_sum = 0 # 到現在這個數字最小的總和 > 減去時才可以減去最多
        min_sub = 0 # 到現在這個數字的前面一個數字 最多可以減去多少 > min(poss_remo 或 min_sum)
        poss_remo = Counter() # 到這個數字 如果扣除的是這個數字 最多可以扣除多少 > min_sum + 這個數字的扣除
        for n in nums :
            now_sum += n
            res = max(res, now_sum - min_sub)
            if n < 0 :
                poss_remo[n] = min(poss_remo[n], min_sum) + n
                min_sub = min(min_sub, poss_remo[n])
            min_sum = min(min_sum, now_sum)
            min_sub = min(min_sub, min_sum)
        return res
    
# # # given ans (after my opt) : segment tree
# # # 7453ms Beats30.09%
# # # 1. 找出所有可能的刪除數字
# # # 2. 組合排除完的數字
# from collections import defaultdict
# class Solution:
#     def __init_node(self, val: int):
#         return (val,val, val, val)

#     def __merge(self, left_node, right_node):
#         total_l, pre_l, suf_l, best_l = left_node
#         total_r, pre_r, suf_r, best_r = right_node

#         total = total_l + total_r
#         prefix = max(pre_l, total_l + pre_r)
#         suffix = max(suf_r, total_r + suf_l)
#         best = max(best_l, best_r, suf_l + pre_r)
#         return (total, prefix, suffix, best)

#     def build_segment_tree(self, arr: list[int]):
#         n = len(arr)
#         self.n = n
#         self.tree = [None]*(4*n)

#         def build(idx, left, right):
#             if left == right:
#                 self.tree[idx] = self.__init_node(arr[left])
#                 return
#             mid = (left+right)//2
#             build(idx*2, left, mid)
#             build(idx*2+1, mid+1, right)
#             self.tree[idx] = self.__merge(self.tree[idx*2], self.tree[idx*2+1])

#         build(1, 0, n-1)

#     def query_segment_tree(self, ql: int, qr: int):
#         def query(idx, left, right, ql, qr):
#             if ql > right or qr < left:
#                 return (0, float('-inf'), float('-inf'), float('-inf'))
#             if ql <= left and right <= qr:
#                 return self.tree[idx]
#             mid = (left+right)//2
#             left_part = query(idx*2, left, mid, ql, qr)
#             right_part = query(idx*2+1, mid+1, right, ql, qr)
#             return self.__merge(left_part, right_part)

#         return query(1, 0, self.n-1, ql, qr)

#     def merge_segments(self, segments):
#         curr = segments[0]
#         for i in range(1, len(segments)):
#             curr = self.__merge(curr, segments[i])
#         return curr
        
#     def maxSubarraySum(self, nums: List[int]) -> int:
#         n = len(nums)
#         if n == 1:
#             return nums[0]

#         neg_pos = defaultdict(list)
#         for i, val in enumerate(nums):
#             if val <= 0:
#                 neg_pos[val].append(i)

#         self.build_segment_tree(nums)
#         ans = self.query_segment_tree(0, n-1)[3] # full range
#         for x, pos in neg_pos.items():
#             if len(pos) == n:
#                 continue
#             seg_nodes = []
#             prev_end = -1
#             for idx in (pos+[n]):
#                 seg_l = prev_end + 1
#                 seg_r = idx - 1
#                 if seg_l <= seg_r: # 如果此兩個 indx 中間沒有其他項目
#                     node = self.query_segment_tree(seg_l, seg_r)
#                     seg_nodes.append(node)
#                 prev_end = idx

#             if not seg_nodes:
#                 continue
#             merged_node = self.merge_segments(seg_nodes)
#             ans = max(ans, merged_node[3])
#         return ans

# my segment tree : 4243ms Beats40.68%
from math import inf
class SegTree:
    def __init__(self, nums):
        self.n = len(nums)
        # init
        self.tree = [(0,0,0,0) for _ in range(self.n)] + [(n,n,n,n) for n in nums]
        for i in range(self.n-1, 0, -1):
            # execute def
            self.tree[i] = SegTree.merge_seg(self.tree[2*i], self.tree[2*i+1])
            
    def merge_seg(segl, segr):
        # sum, 從左邊的底來最大和, 從右邊的底來最大和, best_range_sum
        total_l, max_sum_L_l, max_sum_R_l, best_l = segl
        total_r, max_sum_L_r, max_sum_R_r, best_r = segr
        return (
            total_l + total_r, 
            max(max_sum_L_l, total_l + max_sum_L_r),
            max(max_sum_R_r, total_r + max_sum_R_l),
            max(best_l, best_r, max_sum_R_l + max_sum_L_r))

    def query(self, left, right):
        # not include
        left += self.n+1
        right += self.n-1
        l_res = (0, -inf, -inf, -inf)
        r_res = (0, -inf, -inf, -inf)
        while left <= right:
            if left & 1 :
                # combine result
                l_res = SegTree.merge_seg(l_res, self.tree[left])
                left += 1
            if not (right & 1) :
                # combine result
                r_res = SegTree.merge_seg(self.tree[right], r_res)
                right -= 1
            left >>= 1
            right>>= 1
        return SegTree.merge_seg(l_res, r_res)
    
from collections import defaultdict
class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        neg_pos = defaultdict(list)
        for i, val in enumerate(nums):
            if val <= 0:
                neg_pos[val].append(i)

        e = len(nums)
        segtree = SegTree(nums)
        ans = max(sum(nums), nums[0]) # 有可能會沒有負數 跟 全部都是同一個負數
        for _era_num, pos in neg_pos.items():
            pre_i = -1
            mem = (0, -inf, -inf, -inf)
            for i in pos + [e] :
                ret = segtree.query(pre_i, i)
                mem = SegTree.merge_seg(mem, ret)
                pre_i = i
            ans = max(ans, mem[3])
        return ans
                


        


s = Solution()
# print("ans :",s.maxSubarraySum([-3,2,-2,-1,3,-2,3])) # 7
# print("ans :",s.maxSubarraySum([1,2,3,4])) # 10
# print("ans :",s.maxSubarraySum([4,-6,9,-7,4])) # 13
# print("ans :",s.maxSubarraySum([-3,-3,6,-9,6,-3,-3])) # 12
# print("ans :",s.maxSubarraySum([4,-3,4,-3,4,-3,4])) # 16
# print("ans :",s.maxSubarraySum([-2,-2,-2])) # -2
print("ans :",s.maxSubarraySum([-24,-29,45,48,-32,25,11,-7,27,-21,-38,-35,47,39,-48,-48])) # 149 [45,48,25,11,-7,27]
# print("ans :",s.maxSubarraySum([45,48,-32,25,11,-7,27,-21,-38,-35,47,39])) # 149
# print(sum([45,48,-32,25,11,-7,27,-21,-38,-35,47,39]))
# print(sum([45,48,-32,25,11,-7,27]))
# print(sum([45,48,25,11,-7,27]))
# print("ans :",s.maxSubarraySum([45,48,-32,25,11,-7,27,-21,-38,-35,47])) # merge



