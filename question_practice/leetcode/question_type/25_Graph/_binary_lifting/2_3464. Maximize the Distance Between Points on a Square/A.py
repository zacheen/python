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
        # print(points)

        # O(k^2)
        def check_valid(dis_thresh):
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

        # 如果k大於25，則需要引入倍增演算法 : 303ms Beats93.75% 
        # (雖然比較慢，但是 k 大的時候會比較快) O(klogk)
        #     倍增時需要根據dis_thresh，求距離>=dis_thresh的下一個點的位置，建構倍增訊息
        #     然後針對每個點，計算k個點後的位置，確定最後一個點是否合法
        #         此方法較快的原因是 建立倍增訊息 就找出每個點跳k之後的點了
        # max_bit_len = k.bit_length()  
        # k -= 1 # 跳 k-1 格就好 最後一格 
        # def check_valid(dis_thresh):
        #     # # 建構 parents (一個 child 只能有一個 father)
        #     next_node = [len_n]*len_n
        #     r = 0
        #     for l in range(len_n):
        #         while r < len_n and points[r] - points[l] < dis_thresh:
        #             r += 1
        #         next_node[l] = r
                
        #     # 建構 倍增演算法(binary lifting)
        #     bin_lift = [next_node]+[[len_n]*len_n for _ in range(max_bit_len)]
        #     # bin_lift[parent_lv][node]
        #     now_lv = bin_lift[0]
        #     for lv in range(1, max_bit_len+1):
        #         next_lv = bin_lift[lv]
        #         for node in range(len_n):
        #             if (par:=now_lv[node]) == len_n: continue
        #             next_lv[node] = now_lv[par]

        #     # check all possible start point 
        #     for poss_st in range(0, next_node[0]) :
        #         en_node = poss_st
        #         for shift in range(max_bit_len):
        #             if k >> shift & 1:
        #                 en_node = bin_lift[shift][en_node]
        #                 if en_node == len_n:
        #                     break
        #         else :
        #             if total_len - (points[en_node] - points[poss_st]) >= dis_thresh:
        #                 return True
        #     return False

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

s = Solution()
print("ans :",s.maxDistance(side = 2, points = [[0,2],[2,0],[2,2],[0,0]], k = 4)) # 2
print("ans :",s.maxDistance(side = 2, points = [[0,0],[1,2],[2,0],[2,2],[2,1]], k = 4)) # 1
print("ans :",s.maxDistance(side = 2, points = [[0,0],[0,1],[0,2],[1,2],[2,0],[2,2],[2,1]], k = 5)) # 1
print("ans :",s.maxDistance(side = 2, points = [[0,0],[0,1],[0,2],[1,2],[1,0],[2,0],[2,2],[2,1]], k = 4)) # 2
print("ans :",s.maxDistance(side = 66, points = [[0,50],[66,36],[0,9],[5,0],[46,66],[66,23],[0,36]], k = 4)) # 55



