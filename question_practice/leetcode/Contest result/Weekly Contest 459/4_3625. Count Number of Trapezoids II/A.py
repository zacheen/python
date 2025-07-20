# 3625. Count Number of Trapezoids II
# https://leetcode.com/problems/count-number-of-trapezoids-ii

from typing import List
from math import inf
from collections import defaultdict, Counter

# my fail : 會有重複計算的 應該要扣除平行四邊形
    # inspire by given ans : 平行四邊形 對角中點 會是同一個點
# fail 2 : 要先整數運算 再進行除的運算 才會精準
class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        slop_cnt = defaultdict(Counter)
        para_cnt = defaultdict(Counter)
        ver_cnt = Counter()
        for i, (x1, y1) in enumerate(points) :
            for x2, y2 in points[:i] :
                dy = y1-y2
                dx = x1-x2
                new_slo = dy/dx if dx != 0 else inf
                offset = (x1*dy-y1*dx)/dx if dx != 0 else x1
                # 一定要先整數運算 再進行除的運算 才會精準
                # offset = y1 - (new_slo*x1) if dx != 0 else x1
                slop_cnt[new_slo][offset] += 1

                # for Parallelogram
                # mid_p =( (x1+x2)/2 , (y1+y2)/2 )
                # optimized
                mid_p =( (x1+x2) , (y1+y2) )
                para_cnt[mid_p][new_slo] += 1 # 需要 new_slo，因為還是要避免連成一條線的情況
        # print(ver_cnt)
        # print(list(ver_cnt.values()))
        # print(list(cnt.values() for s, cnt in slop_cnt.items()))
        
        ans = 0
        for _slo, cnt in slop_cnt.items():
            past_snt = 0
            for _offset, n in cnt.items():
                ans += past_snt*n
                past_snt += n

        for _mid_p, cnt in para_cnt.items():
            past_snt = 0
            for _slo, n in cnt.items():
                ans -= past_snt*n
                past_snt += n

        return ans

s = Solution()
print("ans :",s.countTrapezoids([[-3,2],[3,0],[2,3],[3,2],[2,-3]])) # 2
print("ans :",s.countTrapezoids([[0,0],[1,0],[0,1],[2,1]])) # 1
print("ans :",s.countTrapezoids([[71,-89],[-75,-89],[-9,11],[-24,-89],[-51,-89],[-77,-89],[42,11]])) # 
print("ans :",s.countTrapezoids([[0,0],[1,0],[0,1],[2,1]])) # 

