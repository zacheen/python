# 3534. Path Existence Queries in a Graph II
# https://leetcode.com/problems/path-existence-queries-in-a-graph-ii

from typing import List
from math import inf
from collections import defaultdict

# my (binary lifting) 995ms Beats86.80%
class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        # 這題其實就是 找到一條遞增的路徑 從st到en
            # 且每次遞增最好都遞增到小於 maxDiff 的最大值 (因此其實小於此值的路徑都不需要考慮)
        
        len_n = len(nums)
        # 直接使用 nums 排序 indx 對應的 數字 
            # nums[ord_nums[i+1]] > nums[ord_nums[i]]
        ord_nums = list(range(len_n))
        ord_nums.sort(key=nums.__getitem__)
        
        # 先找到每個數字的最遠可以到的數字 (但是是用node代表數字)
        next_far_n = [-1] * len_n
        
        # 使用 for l_i in ord_nums (因為每個 next_far_n[l_i] 都要給值，所以這種應該比較值直觀)
        r = 0
        for l_i in ord_nums :
            l_n = nums[l_i]
            while r < len_n and nums[ord_nums[r]] - l_n <= maxDiff :
                if r == len_n :
                    break
                else :
                    r += 1
            next_far_n[l_i] = ord_nums[r-1]
        
        # # 使用 for r, r_i in enumerate(ord_nums) :
        # l = 0
        # for r, r_i in enumerate(ord_nums) :
        #     r_n = nums[r_i]
        #     while r_n - nums[ord_nums[l]] > maxDiff :
        #         next_far_n[ord_nums[l]] = ord_nums[r-1]
        #         l += 1
        # for l in range(l,len_n) :   
        #     next_far_n[ord_nums[l]] = r_i

        # 把回到自己的路徑設成-1 (binary lifting 才不會出錯)
        for st, end in enumerate(next_far_n):
            if st == end :
                next_far_n[st] = -1

        # 建構 倍增演算法(binary lifting)
        max_bit_len = n.bit_length()
        bin_lift = [next_far_n]+[[-1]*len_n for _ in range(max_bit_len)]
        # bin_lift[parent_lv][node]
		# 用來記錄 [父節點, 父節點的父節點, (父節點)**4, (父節點)**8...] 是誰
            # 這樣找 kth_ancestor 就可以在 O(logn) 的時間內做到
                # 例如 k = 13 = 往上1+往上4+往上8
        now_lv = bin_lift[0]
        for lv in range(1, max_bit_len+1):
            next_lv = bin_lift[lv]
            for node in range(len_n):
                if (par:=now_lv[node]) == -1: continue
                next_lv[node] = now_lv[par]
            now_lv = next_lv

        ans = []
        for st, en in queries :
            if st == en :
                ans.append(0)
                continue
            elif nums[st] == nums[en] :
                ans.append(1)
                continue
            if nums[en] < nums[st] :
                st, en = en, st
            ans_cou = 0
            en_num = nums[en]
            for shift in range(max_bit_len-1,-1,-1):
                next_node = bin_lift[shift][st]
                if next_node != -1 and nums[next_node] < en_num :
                    st = next_node
                    ans_cou += 1 << shift
            if (ne:=bin_lift[0][st]) != -1 and nums[ne] >= en_num :
                ans.append(ans_cou+1)
            else :
                ans.append(-1)
        return ans



s = Solution()
# print("ans :",s.pathExistenceQueries(n = 5, nums = [1,8,3,4,2], maxDiff = 3, 
#     queries = [[0,3],[2,4]])) # [1,1]
# print("ans :",s.pathExistenceQueries(n = 5, nums = [5,3,1,9,10], maxDiff = 2, 
#     queries = [[0,1],[0,2],[2,3],[4,3]])) # [1,2,-1,1]
# print("ans :",s.pathExistenceQueries(n = 3, nums = [3,6,1], maxDiff = 1, 
#     queries = [[0,0],[0,1],[1,2]])) # [0,-1,-1]
# print("ans :",s.pathExistenceQueries(n = 2, nums = [15,15], maxDiff = 18, 
#     queries = [[0,0],[1,1],[1,0]])) # [0,0,-1]
print("ans :",s.pathExistenceQueries(n = 3, nums = [13,17,16], maxDiff = 8, 
    queries = [[1,2]])) # [1]
# print("ans :",s.pathExistenceQueries(n = 16, 
#     nums = [74841,72151,17118,58043,30796,14069,64189,23174,42898,93411,46424,61079,27561,38339,50344,64426], 
#     maxDiff = 7570, queries = [[8,2],[6,9]])) # 



