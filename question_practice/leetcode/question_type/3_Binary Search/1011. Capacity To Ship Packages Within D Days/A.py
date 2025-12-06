# 1011. Capacity To Ship Packages Within D Days
# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/

# my 155ms Beats82.88%
class Solution(object):
    def shipWithinDays(self, weights, days):
        def check(max_cap):
            now_sum = 0
            now_days = 1
            for w in weights:
                now_sum += w
                if now_sum > max_cap :
                    now_days += 1
                    if now_days > days :
                        return False
                    now_sum = w
            return True

        r = sum(weights)
        l = max(weights)
        while l < r-1 :
            mid = (l + r) >> 1
            if check(mid) :
                r = mid
            else :
                l = mid
        
        if check(l) :
            return l
        else :
            return r

s = Solution()
print(s.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)) # 15
print(s.shipWithinDays(weights = [3,2,2,4,1,4], days = 3)) # 6
print(s.shipWithinDays(weights = [1,2,3,1,1], days = 4))  # 4
print(s.shipWithinDays(weights = [1,10,1], days = 2)) #  11 (不能先載 兩個1 再載10)
