# 1383. Maximum Performance of a Team
# https://leetcode.com/problems/maximum-performance-of-a-team/description/
    # Same as 2542. Maximum Subsequence Score，不過這題是不固定長度
from typing import List
from math import inf
from heapq import heapify, heapreplace

# my 76ms Beats75.40%
MOD = 10**9+7
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        best_speed = [0]
        now_s_sum = 0
        ans = 0
        info_p = [(e,s) for e,s in zip(efficiency, speed)]
        info_p.sort(reverse = True)
        # e 會從大取到小 > 所以 e 就會是每次的 min_eff
        for e,s in info_p :
            if len(best_speed) >= k:
                if s > best_speed[0] :
                    now_s_sum += s - heapreplace(best_speed, s)
                    # 不能這裡先MOD 因為是要找最大值 
                        #  MOD 之後 max() 的比較就不準了
                    ans = max(ans, e*now_s_sum)
            else :
                best_speed.append(s)
                now_s_sum += s
                ans = max(ans, e*now_s_sum)
                if len(best_speed) == k:
                    heapify(best_speed)
        return ans % MOD
    
# given ans

s = Solution()
print("ans :",s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2)) # 60
print("ans :",s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3)) # 68
print("ans :",s.maxPerformance(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4)) # 72 = 18*4 (0,1,3,4)
print("ans :",s.maxPerformance(n = 3, speed = [2,8,2], efficiency = [2,7,2], k = 2)) # 56 = 8*7 (1)



