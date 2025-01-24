# 思考 : 有時候換方向做 反而比較簡單

# my practice again : 205ms Beats5.33%
# still forget that other way is faster
from math import inf
from bisect import bisect_right
from collections import deque
class Solution:
    def find132pattern(self, nums):
        poss_left = nums[0]
        stack = deque([(inf,inf)])
        for n in nums :
            # check valid
            if n > stack[0][0]:
                r = stack[bisect_right(stack, n, key=lambda x : x[0])-1]
                if n < r[1] : # because bisect so don't need "n > r[0]"
                    return True
            # update
            if n > poss_left :
                top = n
                while stack[0][0] <= n :
                    top = max(top, stack.popleft()[1])
                stack.appendleft((poss_left, top))
            poss_left = min(poss_left, n)
        return False

# given ans Runtime: 47ms Beats78.07%
# 我剛剛是要找中間的點
# 它反方向來看 先找到有無 儲存second > third 儲存third
# 在判斷有沒有點 在third之下
class Solution:
    def find132pattern(self, nums):
        stack = [] # max stack
        ak = -1000000001  # we want to find a seq ai < ak < aj
        for i in range (len(nums)-1, -1, -1) :
            # 有 ak 代表之前已經找到 上升的點了 所以小於ak就有答案
            if nums[i] < ak : 
                return True
            # 如果 此點 > stack中最大的點
            # 目標是找到 最大的 ak
            while stack and stack[-1] < nums[i] :
                ak = stack.pop()
            stack.append(nums[i]) # stack 裡面是存 ak 的候選數字 # 只是由於目前沒有找到比 此數更大的數字
        return False

s = Solution()
print(s.find132pattern([3,1,4,2])) # [1,4,2] # T
print(s.find132pattern([1,4,0,-1,-2,-3,-1,-2])) # [-3,-1,-2] # T
print(s.find132pattern([3,5,0,1,2,4])) # [3,5,3] # T

# print(s.find132pattern([1,4,0,5,-1]))
# print(s.find132pattern([1,4,0,3,-1]))
# print(s.find132pattern([1,4,-10,-5,-11]))
# print(s.find132pattern([3,1,4,0,5,-1,6,-10,7,-11]))
# print(s.find132pattern([42,43,6,12,3,4,6,11,20]))
