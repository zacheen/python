# 3660. Jump Game IX
# https://leetcode.com/problems/jump-game-ix/

from typing import List
from math import inf

# my inspired by given ans, 127ms Beats99.58%
class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        # 往右 要變小
        # 往左 要變大

        # logic
        # 1. 左邊比較大 就一定能跳過去 > 最佳結果最後一定是往左跳 或 待在原地
        # 2. 往右跳的時候 若能跳到此點 一定能跳到此點的最佳位置 (DP)
            # [5,2,3,8,4,9,7] -> 3>5>4>8>7>9 
            # 所以後面的點的結果應該要先完成
        
        # 先找到各個位置左邊最大的數值
        max_left = []
        now_max = 0
        for n in nums :
            if n > now_max :
                now_max = n
            max_left.append(now_max)

        # 找到各個位置右邊最小的數值 (為了確定能跳到右邊)
        min_right = []
        now_min = nums[-1]
        for n in nums[::-1] :
            if n < now_min :
                now_min = n
            min_right.append(now_min)
        min_right = min_right[::-1]

        # print(max_left)
        # print(min_right)

        # 只要判斷右邊有沒有更小的點 就能判斷能不能走到此點右邊最佳的結果
        # (只要能往右 最佳結果一定與此點右邊相同 因為一定能走到)
        res = max_left.copy()
        for i in range(len(nums)-2, -1, -1) :
            if max_left[i] > min_right[i+1] : # 判斷可以往右走 (min_right[i+1] 是因為不能包含自己這點)
                res[i] = res[i+1] # 也不用比較了 因為右邊的點的 logic1 包含所有左邊 logic1 的點
        return res


s = Solution()
print("ans :",s.maxValue([2,1,3])) # [2,2,3]
print("ans :",s.maxValue([2,3,1])) # [3,3,3]
print("ans :",s.maxValue([11,18,11])) # [11,18,18]
print("ans :",s.maxValue([30,21,5,35,24])) # [35,35,35,35,35]
print("ans :",s.maxValue([5,2,4,8,4,9,7])) # [35,35,35,35,35]
# 變大可以再變小再變大

