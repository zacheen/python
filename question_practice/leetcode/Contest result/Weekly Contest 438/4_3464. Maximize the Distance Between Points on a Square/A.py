# 3464. Maximize the Distance Between Points on a Square
# https://leetcode.com/problems/maximize-the-distance-between-points-on-a-square/description/

from typing import List
from math import inf
from collections import defaultdict
from functools import cache
from bisect import bisect_left

# given ans : 27ms Beats100.00%
class Solution:
    def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
        # points = [-sum(x) if x[0] > x[1] else sum(x) for x in points]
        len_n = len(points)
        total_len = side*4

        points = [-sum(x)+total_len if x[0] > x[1] else sum(x) for x in points]
        points.sort()
        print(points)
            
        def check_valid(dis_thresh):
            # 如果k大於25，則需要引入倍增演算法。倍增時需要根據dis_thresh，求距離>=dis_thresh的下一個點的位置，建構倍增訊息
            # 然後針對每個點，計算k個點後的位置，確定最後一個點是否合法
            
            # 為什麼只需要計算 從第一個點開始 就可以知道是否會 return False ??
                # 這裡只有判斷 第一個點 到 最後一個點 是否有在限制之內
                    # 沒有判斷最後一個點到第一個點的距離是否合規則
                # 如果光是少一個點都不行了，那其他開頭的循環距離一定也不行
            next_node = [0]
            cur = points[0]
            for j in range(1, k):
                i = bisect_left(points, cur + dis_thresh)
                if i == len_n:
                    return False
                next_node.append(i)
                cur = points[i]
            
            # 判斷以第一個點開始 是否可以合乎規則 
            if total_len - (cur - points[0]) >= dis_thresh:
                return True
            
            # 判斷其他點開頭是否可行
            # 其他可能的開頭只有第一個點到第二個點之間
            for next_node[0] in range(next_node[0]+1, next_node[1]):
                for j in range(1, k):
                    while points[next_node[j]] - points[next_node[j - 1]] < dis_thresh:
                        next_node[j] += 1
                        if next_node[j] == len_n:
                            return False
                if total_len - (points[next_node[-1]] - points[next_node[0]]) >= dis_thresh:
                    return True
            return False

        left = 1
        right = side
        while left + 1 < right:
            mid = (left + right) // 2
            # 這裡我移除 少一次判斷
            # if nums[mid] == target:
            #     return mid
            if check_valid(mid):
                left = mid
            else:
                right = mid

        # End Condition: left + 1 == right
        if check_valid(right): return right # right 先做，如果希望結果愈大愈好!
        return left

# # optimized by given ans : 606ms Beats61.47%
# class Solution:
#     def maxDistance(self, side: int, points: List[List[int]], k: int) -> int:
#         # points = [-sum(x) if x[0] > x[1] else sum(x) for x in points]
#         len_n = len(points)
#         total_len = side*4

#         points = [-sum(x)+total_len if x[0] > x[1] else sum(x) for x in points]
#         points.sort()
#         points += [n+total_len for n in points]
#         # print(points)

#         # no needed, since max distance is side
#         # def cal_len(n1,n2):
#         #     if (t:=abs(n1-n2)) > half_len :
#         #         return total_len - t
#         #     else :
#         #         return t
            
#         def check_valid(dis_thresh):
#             r = 1
#             # find the nearest point is the best decision
#             find_next_node = []
#             for p in points :
#                 while r < len(points) and points[r] - p < dis_thresh : # actually total time complexity is O(n)
#                     r += 1
#                 if r == len(points) :
#                     break
#                 find_next_node.append(r)
#             find_next_node += [inf]*(len(points)-len(find_next_node))
            
#             def dfs(i, d):
#                 count = 1
#                 cur = i
#                 limit = points[i] + total_len - dis_thresh
#                 while count < k:
#                     cur = find_next_node[cur]
#                     if cur == inf:
#                         return False
#                     if points[cur] > limit:
#                         return False
#                     count += 1
#                 return True
            
#             for start_n in range(len_n):
#                 if dfs(start_n, k) :
#                     return True
#             return False

#         left = 1
#         right = side
#         while left + 1 < right:
#             mid = (left + right) // 2
#             # 這裡我移除 少一次判斷
#             # if nums[mid] == target:
#             #     return mid
#             if check_valid(mid):
#                 left = mid
#             else:
#                 right = mid

#         # End Condition: left + 1 == right
#         if check_valid(right): return right # right 先做，如果希望結果愈大愈好!
#         return left

# my 744ms Beats53.19%
    # fast forward is actually slower
    # mine might be faster when limitation of k is bigger 
# def check_valid(dis_thresh):
#     r = 1
#     # find the nearest point is the best decision
#     find_next_node = []
#     for p in points :
#         while r < len(points) and points[r] - p < dis_thresh : # actually total time complexity is O(n)
#             r += 1
#         if r == len(points) :
#             break
#         find_next_node.append(r)
#     find_next_node += [inf]*(len(points)-len(find_next_node))
    
#     ff = {} # ff[node] = [ff_num, final_node]
#     def dfs(now_node_i, remain) :
#         nonlocal ff
#         if remain == 0 :
#             return 0, now_node_i
#         if now_node_i in ff :
#             ff_num, final_node = ff[now_node_i]
#             if final_node == inf :
#                 return -inf, inf
#             ret_f_num, final_node = dfs(final_node, remain-ff_num)
#             ret_f_num += ff_num
#             res = (ret_f_num, final_node)
#             ff[now_node_i] = res
#             return res
        
#         next_node = find_next_node[now_node_i]
#         if next_node == inf :
#             return -inf, inf
#         cou, final_node = dfs(next_node, remain-1)
#         cou += 1
#         res = (cou, final_node)
#         ff[now_node_i] = res
#         return res
    
#     for start_n in range(len_n):
#         _, final_node = dfs(start_n, k)
#         if final_node - len_n <= start_n :
#             return True
#     return False

s = Solution()
print("ans :",s.maxDistance(side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4)) # 2
print("ans :",s.maxDistance(side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4)) # 1
print("ans :",s.maxDistance(side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5)) # 1
print("ans :",s.maxDistance(side = 2, points = [[0,0],[0,1],[0,2],[1,2],[1,0],[2,0],[2,2],[2,1]], k = 4)) # 2
print("ans :",s.maxDistance(side = 66, points = [[0,50],[66,36],[0,9],[5,0],[46,66],[66,23],[0,36]], k = 4)) # 55



