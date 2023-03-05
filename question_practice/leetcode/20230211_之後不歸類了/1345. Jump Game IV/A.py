# 1345. Jump Game IV
# my v2 Beats 93.82%
from collections import defaultdict
class Solution:
    def minJumps(self, arr):
        # 先建立連結 才知道相同的數字可以走到哪裡
        # BFS

        link_set = defaultdict(set)
        # 看解答 : 因為 link_set 沒有要判斷有沒有重複的項目 所以應該是用 List 比較快
        for indx, val in enumerate(arr):
            link_set[val].add(indx)
        # print(link_set)

        mem_not_walk_before = {}
#         # 這裡可以用兩種方法 mem 
#             # 紀錄走過的位置 (5 * 10^4 應該還好) 結果沒有辦法實作 走過的數字 所以我換下面的方法
#                 # mem_walk_before = [False]*len(arr)
#             # 紀錄走過的數字 <- 應該比較快 (記得 : 查找有沒有重複的項目用 hash 最快)
        stack = {0}
        end_point = len(arr) - 1
        step_count = 0
        while stack :
            next_stack = set() # 我不確定 set 比較快 還是 list # 沒想到快超多 (但我不知道為什麼快這麼多??)
            # print(stack)
            for p in stack :
                if p == end_point :
                    return step_count
                # same num
                if mem_not_walk_before.get(arr[p], True) :
                    next_stack |= link_set[arr[p]]
                # 這個放這裡有優化的意思
                mem_not_walk_before[arr[p]] = False
                # +1
                if mem_not_walk_before.get(arr[p+1], True):
                    next_stack.add(p+1)
                # -1
                if (p-1 > 0) and mem_not_walk_before.get(arr[p-1], True) :
                    next_stack.add(p-1)
                if p in next_stack :
                    next_stack.remove(p)
            step_count += 1
            stack = next_stack
        return -1

# # my v1 Time Limit Exceeded
# from collections import defaultdict
# class Solution:
#     def minJumps(self, arr):
#         # 先建立連結 才知道相同的數字可以走到哪裡
#         # BFS

#         link_set = defaultdict(set)
#         for indx, val in enumerate(arr):
#             link_set[val].add(indx)
#         # print(link_set)

#         mem_not_walk_before = {}
#         # 這裡可以用兩種方法 mem 
#             # 紀錄走過的位置 (5 * 10^4 應該還好) 結果沒有辦法實作 走過的數字 所以我換下面的方法
#                 # mem_walk_before = [False]*len(arr)
#             # 紀錄走過的數字 
#         # print("mem_walk_before[100] :",mem_not_walk_before.get(100, True))
#         # mem_not_walk_before[100] = False
#         # print("mem_walk_before[100] :",mem_not_walk_before.get(100, True))
        
#         stack = [0]
#         end_point = len(arr) - 1
#         step_count = 0
#         while True :
#             next_stack = [] # 我不確定 set 比較快 還是 list
#             # print(stack)
#             for p in stack :
#                 if p == end_point :
#                     return step_count
#                 # same num
#                 if mem_not_walk_before.get(arr[p], True) :
#                     next_stack += list(link_set[arr[p]])
#                 mem_not_walk_before[arr[p]] = False
#                 # +1
#                 if mem_not_walk_before.get(arr[p+1], True):
#                     next_stack.append(p+1)
#                 # -1
#                 if (p-1 > 0) and mem_not_walk_before.get(arr[p-1], True) :
#                     next_stack.append(p-1)
#             step_count += 1
#             stack = next_stack
#         return 

# given ans
# 概念相同

s = Solution()
print(s.minJumps([100,-23,-23,404,100,23,23,23,3,404]))
print(s.minJumps([7]))
print(s.minJumps([7,6,9,6,9,6,9,7]))



