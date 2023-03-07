# my Beats 96.15%
class Solution(object):
    def minimumTime(self, time, totalTrips):
        def check_able(total_days):
            total_trip = sum([total_days//days for days in time])
            # print("in check_able : ", total_trip)
            
            # 可以縮寫 ##############
            # if total_trip >= totalTrips :
            #     return True
            # else :
            #     return False
            # 精簡後 
            return total_trip >= totalTrips
        
        # 使用 binarySearch_adv
        left, right = 1, (totalTrips*min(time)+1)
        print(left, right)
        while left + 1 < right:
            mid = (left + right) // 2
            # print("mid : ", mid)
            if not check_able(mid):
                left = mid
            else:
                right = mid

        if check_able(left): 
            return left
        return right

# given ans
# 邏輯一樣 但是用不同的 template 所以更簡潔
class Solution(object):
    def minimumTime(self, time, totalTrips):
        l = 1
        r = min(time) * totalTrips

        while l < r:
            m = (l + r) // 2
            if sum(m // t for t in time) >= totalTrips:
                r = m
            else:
                l = m + 1

        return l

s = Solution()
print(s.minimumTime(time = [1,2,3], totalTrips = 5))
print(s.minimumTime(time = [2], totalTrips = 1))



