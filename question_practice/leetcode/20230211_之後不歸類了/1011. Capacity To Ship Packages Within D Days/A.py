# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/description/
# my Beats 76%
class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """

        left = max(weights)
        right = sum(weights)
        # print(left, right)

        def check_cost_days(capacity_weight):
            now_total_weight = 0
            total_days = 1
            for w in weights :
                now_total_weight += w
                if now_total_weight > capacity_weight :
                    total_days += 1
                    now_total_weight = w
            # print("in check_cost_days", capacity_weight, total_days)
            return total_days

        while left + 1 < right:
            mid = (left + right) // 2
            if check_cost_days(mid) > days:
                left = mid
            else:
                right = mid

        # End Condition: left + 1 == right
        if check_cost_days(left) <= days: return left
        else : return right

# given ans

s = Solution()
print(s.shipWithinDays(weights = [1,2,3,4,5,6,7,8,9,10], days = 5)) # 15
print(s.shipWithinDays(weights = [3,2,2,4,1,4], days = 3)) # 6
print(s.shipWithinDays(weights = [1,2,3,1,1], days = 4))  # 4
print(s.shipWithinDays(weights = [1,10,1], days = 2)) #  11 (不能先載 兩個1 再載10)
