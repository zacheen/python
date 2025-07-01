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
                
# my using SegTree template 2 : 6753ms Beats19.70%  
class SegTree:
    def __init__(self, nums):
        self.default_value = None
        self.n = len(nums)
        self.tree = [self.default_value] * (4 * self.n)
        def build_rec(tree_idx, seg_st, seg_en):
            if seg_st == seg_en:
                self.tree[tree_idx] = (nums[seg_st], nums[seg_st], nums[seg_st], nums[seg_st]) 
                return
            mid = (seg_st + seg_en) >> 1
            tree_idx_l = tree_idx << 1
            tree_idx_r = tree_idx_l + 1
            build_rec(tree_idx_l, seg_st, mid)
            build_rec(tree_idx_r, mid + 1, seg_en)
            self._update_node(tree_idx, tree_idx_l, tree_idx_r)
        build_rec(1, 0, self.n-1)

    def _merge_val(self, l, r):
        l_sum, l_left_max, l_right_max, l_max_sum = l
        r_sum, r_left_max, r_right_max, r_max_sum = r
        
        return (
            l_sum + r_sum,
            max(l_left_max, l_sum + r_left_max),
            max(r_right_max, r_sum + l_right_max),
            max(l_max_sum, r_max_sum, l_right_max + r_left_max)
        )
    
    def _update_node(self, tree_idx, tree_idx_l, tree_idx_r) :
        self.tree[tree_idx] = self._merge_val(self.tree[tree_idx_l], self.tree[tree_idx_r])

    # def update(self, index, value):
    #     def update_rec(tree_idx, seg_st, seg_en):
    #         if seg_st == index and index == seg_en:  # Entire segment is target index
    #             self.tree[tree_idx] = value
    #         else: # Update nested segments that contain the target index
    #             mid = (seg_st + seg_en) >> 1
    #             tree_idx_l = tree_idx << 1
    #             tree_idx_r = tree_idx_l + 1
    #             if index <= mid:
    #                 update_rec(tree_idx_l, seg_st, mid)
    #             else:
    #                 update_rec(tree_idx_r, mid + 1, seg_en)
    #             self._update_node(tree_idx, tree_idx_l, tree_idx_r)
    #     update_rec(1, 0, self.n - 1)

    def query(self, q_left, q_right): # include both q_left, q_right
        def query_rec(tree_idx, seg_st, seg_en):
            if q_right < seg_st or seg_en < q_left :  # No overlap
                return [0,0,0,0]
            elif q_left <= seg_st and seg_en <= q_right:  # Full overlap
                return self.tree[tree_idx]
            else:  # Partial overlap
                mid = (seg_st + seg_en) >> 1
                tree_idx_l = tree_idx << 1
                tree_idx_r = tree_idx_l + 1
                left_ret = query_rec(tree_idx_l, seg_st, mid)
                right_ret = query_rec(tree_idx_r, mid + 1, seg_en)
                return self._merge_val(left_ret, right_ret)
        return query_rec(1, 0, self.n-1)

class Solution:
    def maxSubarraySum(self, nums: List[int]) -> int:
        mem_pos = defaultdict(list)
        neg_cou = 0
        for i, n in enumerate(nums):
            if n < 0 :
                mem_pos[n].append(i)
                neg_cou += 1
        
        if neg_cou == len(nums) :
            return max(nums)
        if neg_cou == 0 :
            return sum(nums)

        segtree = SegTree(nums)
        ans = 0
        end_i = len(nums)
        for neg_n, pos in mem_pos.items() :
            now_info = [0,0,0,0]
            last_i = 0
            for neg_i in pos + [end_i] :
                if (en:=neg_i-1) >= last_i :
                    ret = segtree.query(last_i, en)
                    now_info = segtree._merge_val(now_info, ret)
                last_i = neg_i+1
            ans = max(ans, max(now_info[1:]))
        return ans

s = Solution()
print("ans :",s.maxSubarraySum([-3,2,-2,-1,3,-2,3])) # 7
print("ans :",s.maxSubarraySum([1,2,3,4])) # 10
print("ans :",s.maxSubarraySum([4,-6,9,-7,4])) # 13
print("ans :",s.maxSubarraySum([-3,-3,6,-9,6,-3,-3])) # 12
print("ans :",s.maxSubarraySum([4,-3,4,-3,4,-3,4])) # 16
print("ans :",s.maxSubarraySum([-2,-2,-2])) # -2
print("ans :",s.maxSubarraySum([-31,-23,-47])) # -23
# print("ans :",s.maxSubarraySum([-24,-29,45,48,-32,25,11,-7,27,-21,-38,-35,47,39,-48,-48])) # 149 [45,48,25,11,-7,27]
# print("ans :",s.maxSubarraySum([45,48,-32,25,11,-7,27,-21,-38,-35,47,39])) # 149
# print(sum([45,48,-32,25,11,-7,27,-21,-38,-35,47,39]))
# print(sum([45,48,-32,25,11,-7,27]))
# print(sum([45,48,25,11,-7,27]))
# print("ans :",s.maxSubarraySum([45,48,-32,25,11,-7,27,-21,-38,-35,47])) # merge



