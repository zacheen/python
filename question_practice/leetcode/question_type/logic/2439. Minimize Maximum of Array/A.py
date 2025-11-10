# my Beats 81.17%
from math import ceil
class Solution:
    def minimizeArrayValue(self, nums):
        # 前面 +1 後面 -1
        # 數字只能往前推
            # 我一開始的想法是(錯誤的想法) : 
                # 因為數字只能往前推，所以我應該從前面找最佳解
                # 也就是從前面開始計算說，現在這兩個數字的最佳解
                # 但後來想到有 1,1,1,10 這種 test case 才意識到是錯的
            # 後來我也不知道我怎麼靈機一動，想到要計算平均的
            # 目前沒想到有什麼有系統的方法，可以幫我整理出對的結論...
        max_average = 0 
        now_sum = 0
        for indx, n in enumerate(nums) :
            now_sum += n
            now_average = ceil(now_sum / (indx+1))
            max_average = max(max_average, now_average)
        return max_average

# given ans
# 完全一樣

s = Solution()
print(s.minimizeArrayValue([3,7,1,6]))
print(s.minimizeArrayValue([10,1]))
print(s.minimizeArrayValue([1,1,1,10]))



