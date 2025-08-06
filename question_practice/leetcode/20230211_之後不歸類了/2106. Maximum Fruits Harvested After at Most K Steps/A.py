# 2106. Maximum Fruits Harvested After at Most K Steps
# https://leetcode.com/problems/maximum-fruits-harvested-after-at-most-k-steps

from typing import List
from math import inf
from bisect import bisect_left, bisect_right

# my 95ms Beats90.00%
class Solution:
    def maxTotalFruits(self, fruits: List[List[int]], startPos: int, k: int) -> int:        
        fruits = [(-inf, 0)] + fruits + [(inf, 0)]
        
        st_i = bisect_left(fruits, startPos, key = lambda x: x[0])
        ans_add = 0
        if fruits[st_i][0] == startPos :
            ans_add = fruits[st_i][1]
            fruits[st_i][1] = 0
        
        ans = 0
        max_ret = k / 3

        # 先找出向右 所有距離可以得到幾個水果
        r = [(-inf,0)]
        now_total = 0
        for pos_i, cnt in fruits[st_i:] :
            dis = pos_i-startPos
            if dis > k :
                break
            now_total += cnt
            r.append((dis, now_total))
        # case 往右走到底
        ans = now_total

        # 找出向左 所有距離可以得到幾個水果，然後計算各種case
        now_total = 0
        if st_i-1 >= 0 :
            for pos_i, cnt in fruits[st_i-1::-1] :
                dis = startPos-pos_i
                if dis > k :
                    break
                now_total += cnt
                if dis <= max_ret : # 一定是先走左 然後迴轉 (因為從另外一邊迴轉會比較遠)
                    rem_dis = k - 2*dis
                    ret_i = bisect_right(r, rem_dis, key = lambda x: x[0])-1
                    if (new_total := now_total + r[ret_i][1]) > ans :
                        ans = new_total
                else : # 一定是先走右 然後迴轉
                    rem_dis = (k - dis) // 2
                    ret_i = bisect_right(r, rem_dis, key = lambda x: x[0])-1
                    if (new_total := now_total + r[ret_i][1]) > ans :
                        ans = new_total
        ans = max(ans, now_total)
        return ans + ans_add

s = Solution()
print("ans :",s.maxTotalFruits(fruits = [[2,8],[6,3],[8,6]], startPos = 5, k = 4)) # 9
print("ans :",s.maxTotalFruits(fruits = [[0,9],[4,1],[5,7],[6,2],[7,4],[10,9]], startPos = 5, k = 4)) # 14
print("ans :",s.maxTotalFruits(fruits = [[0,3],[6,4],[8,5]], startPos = 3, k = 2)) # 0
print("ans :",s.maxTotalFruits(fruits = [[200000,10000]], startPos = 0, k = 0)) # 0
print("ans :",s.maxTotalFruits(fruits = [[0,10000]], startPos = 200000, k = 200000)) # 10000
print("ans :",s.maxTotalFruits(fruits = [[0,7],[7,4],[9,10],[12,6],[14,8],[16,5],[17,8],[19,4],[20,1],[21,3],[24,3],[25,3],[26,1],[28,10],[30,9],[31,6],[32,1],[37,5],[40,9]], startPos = 21, k = 30)) # 10000



