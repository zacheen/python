# 3414. Maximum Score of Non-overlapping Intervals
# https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/description/

from typing import List
import functools

import bisect
from math import inf
# my 1843ms Beats100.00%
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        intervals = [ ((li-1, ri, weighti),i) for i, (li, ri, weighti) in enumerate(intervals)]
        intervals.sort()
        # print(intervals)
        mem = [[] for _ in range(4)]
        max_sum = -1
        max_list = []
        for info, indx in intervals :
            for mem_i in range(3,-1,-1):
                li, ri, weighti = info
                new_item = [ri, weighti, [indx]]
                
                # DP 之前最好的結果
                if mem_i >= 1 :
                    # 從前一個 mem 找到最好的結果
                    _ = mem[mem_i-1]
                    best_indx = bisect.bisect_right(mem[mem_i-1], [li,inf,[]])-1
                    if best_indx < 0 :
                        continue
                    new_item[1] += mem[mem_i-1][best_indx][1]
                    # find the lexicographically smallest
                    best_w = mem[mem_i-1][best_indx][1]
                    same_w_sta = bisect.bisect_left(mem[mem_i-1], best_w, lo=0, hi=best_indx, key=lambda x : x[1])
                    if same_w_sta != best_indx :
                        # print("chech same wei include all same", mem[mem_i-1][same_w_sta:best_indx+1])
                        new_item[2] += min(each[2] for each in mem[mem_i-1][same_w_sta:best_indx+1])
                    else :
                        new_item[2] += mem[mem_i-1][best_indx][2]
                
                # 更新 max
                if new_item[1] > max_sum :
                    new_item[2].sort()
                    max_list = new_item[2]
                    max_sum = new_item[1]
                elif new_item[1] == max_sum :
                    new_item[2].sort()
                    if max_list > new_item[2] :
                        max_list = new_item[2]
                        max_sum = new_item[1]

                # 更新 mem
                ins_indx = bisect.bisect_right(mem[mem_i], [ri,inf,[]])
                # 如果達到更新條件
                if ins_indx == 0 :
                    mem[mem_i].insert(ins_indx, new_item)
                elif new_item[1] > mem[mem_i][ins_indx-1][1] :
                    if ri == mem[mem_i][ins_indx-1][0] :
                        mem[mem_i][ins_indx-1] = new_item
                        ins_indx -= 1
                    else :
                        if ri < mem[mem_i][ins_indx-1][0] : assert Exception
                        mem[mem_i].insert(ins_indx, new_item)
                elif new_item[1] == mem[mem_i][ins_indx-1][1] :
                    if ri == mem[mem_i][ins_indx-1][0] :
                        mem[mem_i][ins_indx-1][2] = min(mem[mem_i][ins_indx-1][2], new_item[2])
                        ins_indx -= 1
                    else :
                        mem[mem_i].insert(ins_indx, new_item)
                # 更新後，剔除不合格的
                while ins_indx < len(mem[mem_i])-1 :
                    if mem[mem_i][ins_indx][1] > mem[mem_i][ins_indx+1][1] :
                        del(mem[mem_i][ins_indx+1])
                    else :
                        break
                    
        #     # print(info, mem)
        #     print("info", info)
        #     for m in mem :
        #         print(m)
        # print("max_sum", max_sum)
        return max_list
    
# given ans 1112ms Beats100.00%
# same logic : for intervals for 4 + bisect
# opt : sorted by "end" > easier to deal "lexicographically smallest"
from typing import List
import bisect
class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        # Enumerate intervals with their original indices
        enumerated_intervals = [
            (interval[0], interval[1], interval[2], idx)
            for idx, interval in enumerate(intervals)
        ]
        
        # Sort intervals based on end time
        enumerated_intervals.sort(key=lambda x: x[1])
        
        # Initialize DP tables for j = 0 to 4
        # Each dp[j] contains tuples of (end_time, total_weight, sequence)
        dp_ends = [[] for _ in range(5)]      # dp_ends[j] stores end times for j intervals
        dp_weights = [[] for _ in range(5)]   # dp_weights[j] stores corresponding weights
        dp_sequences = [[] for _ in range(5)] # dp_sequences[j] stores corresponding sequences
        
        # Initialize dp[0] with a dummy interval ending at time 0
        dp_ends[0].append(0)
        dp_weights[0].append(0)
        dp_sequences[0].append([])
        
        for interval in enumerated_intervals:
            start, end, weight, idx = interval
            # Iterate from 4 down to 1 to avoid using updated dp[j-1] in the same iteration
            for j in range(4, 0, -1):
                if j == 1:
                    # For j == 1, consider taking the current interval alone
                    candidate_weight = weight
                    candidate_sequence = [idx]
                    
                    if not dp_weights[j]:
                        # If no sequence exists for j, add the current one
                        dp_ends[j].append(end)
                        dp_weights[j].append(candidate_weight)
                        dp_sequences[j].append(candidate_sequence)
                    else:
                        # Compare with the last entry
                        last_weight = dp_weights[j][-1]
                        last_sequence = dp_sequences[j][-1]
                        if candidate_weight > last_weight:
                            dp_ends[j].append(end)
                            dp_weights[j].append(candidate_weight)
                            dp_sequences[j].append(candidate_sequence)
                        elif candidate_weight == last_weight:
                            if candidate_sequence < last_sequence:
                                dp_ends[j].append(end)
                                dp_weights[j].append(candidate_weight)
                                dp_sequences[j].append(candidate_sequence)
                else:
                    # For j > 1, find the best sequence for j-1 that doesn't overlap
                    # Use binary search to find the rightmost end_time less than start
                    pos = bisect.bisect_left(dp_ends[j-1], start) - 1
                    if pos >= 0:
                        prev_weight = dp_weights[j-1][pos]
                        prev_sequence = dp_sequences[j-1][pos]
                        candidate_weight = prev_weight + weight
                        candidate_sequence = prev_sequence + [idx]
                        
                        if not dp_weights[j]:
                            # If no sequence exists for j, add the current one
                            dp_ends[j].append(end)
                            dp_weights[j].append(candidate_weight)
                            dp_sequences[j].append(candidate_sequence)
                        else:
                            # Compare with the last entry
                            last_weight = dp_weights[j][-1]
                            last_sequence = dp_sequences[j][-1]
                            if candidate_weight > last_weight:
                                dp_ends[j].append(end)
                                dp_weights[j].append(candidate_weight)
                                dp_sequences[j].append(candidate_sequence)
                            elif candidate_weight == last_weight:
                                if candidate_sequence < last_sequence:
                                    dp_ends[j].append(end)
                                    dp_weights[j].append(candidate_weight)
                                    dp_sequences[j].append(candidate_sequence)
        
        # After processing all intervals, find the best sequence among all j from 1 to 4
        best_weight = 0
        best_sequence = []
        for j in range(1, 5):
            for weight, sequence in zip(dp_weights[j], dp_sequences[j]):
                if weight > best_weight:
                    best_weight = weight
                    best_sequence = sequence
                elif weight == best_weight:
                    if sequence < best_sequence:
                        best_sequence = sequence
        
        # Sort the sequence to get lexicographically smallest order
        return sorted(best_sequence)


# # my : Memory Limit Exceeded
# indx_max = 10**9+1
# class SegTree:
#     def __init__(self):
#         self.n = indx_max
#         # init
#         self.tree = [0] * 2 * self.n

#     def update(self, index, val):
#         index += self.n
#         self.tree[index] = val
#         while index > 1:
#             # update node
#             self.tree[index>>1] = max(self.tree[index], self.tree[index^1])
#             index >>= 1

#     def query(self, right):
#         # include
#         left = self.n
#         right += self.n
#         res = -1
#         while left <= right:
#             if left & 1 :
#                 # combine result
#                 res = max(res, self.tree[left])
#                 left += 1
#             if not (right & 1) :
#                 # combine result
#                 res = max(res, self.tree[right])
#                 right -= 1
#             left >>= 1
#             right>>= 1
#         return res

# class Solution:
#     def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
#         intervals = [ ((li-1, ri, weighti),i) for i, (li, ri, weighti) in enumerate(intervals)]
#         intervals.sort()
#         # print(intervals)
#         mem = [SegTree() for _ in range(4)]

#         for info,i in intervals :
#             range_val = (ri-li)*weighti
#             # mem[0]
#             li, ri, weighti = info
#             mem[0].update( range_val )

#             # mem[1]~mem[3]
#             for i in range(3):
#                 max_prev_wei = mem[i].query(ri)
#                 if max_prev_wei == 0 :
#                     break
#                 mem[i+1].update( range_val+max_prev_wei )
#         print( mem[3].query(indx_max-1) )



s = Solution()
# print("ans :",s.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1]])) # [2,3]
# print("ans :",s.maximumWeight([[1,3,2],[4,5,2],[1,5,5],[6,9,3],[6,7,1],[8,9,1], [2,6,6]])) 
# print("ans :",s.maximumWeight([[5,8,1],[6,7,7],[4,7,3],[9,10,6],[7,8,2],[11,14,3],[3,5,5]])) # [1,3,5,6]
# print("ans :",s.maximumWeight([[17,17,10],[23,23,23],[3,8,31],[17,21,48],[18,24,44]])) # [1, 2, 3]
# print("ans :",s.maximumWeight([[21,22,47],[2,20,49],[21,22,9],[5,14,25],[4,10,46],[23,23,6],[20,25,15],[18,21,32],[25,25,17]])) # [0, 1, 5, 8]
print("ans :",s.maximumWeight([[25,25,36],[2,14,24],[7,17,45],[13,20,17],[14,16,46],[2,16,41]])) # [0, 1, 5, 8]

# for testing lexicographically smallest
# print("ans :",s.maximumWeight([[7,12,50],[16,25,27],[5,10,50]])) # [0,1]
# print("ans :",s.maximumWeight([[19,23,40],[0,16,31],[1,16,31],[16,18,31]])) # [0,1]
# print("ans :",s.maximumWeight([[19,23,40],[1,20,31],[0,16,31],[16,18,31]])) # [0,1]



