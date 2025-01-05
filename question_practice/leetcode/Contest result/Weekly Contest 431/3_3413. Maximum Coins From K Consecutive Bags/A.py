# 3413. Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/description/

from typing import List
import functools

from collections import deque

# my 802ms Beats100.00%
# fail : logic is not correct
# fail : missing fast forward itself : time limit exceed
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        coins.sort()
        # print(coins)
        
        stack = deque()
        max_ans = 0
        now_sum = 0
        for c_range in coins :
            c_range[1] += 1 # change to not include
            stack.append([c_range[0], c_range[0], c_range[2]])            
            # print("app :",stack, max_ans)
            while True : 
                # 先補齊
                max_r = min(stack[0][0] + k, c_range[1])
                now_sum += (max_r - stack[-1][1])*c_range[2]
                stack[-1][1] = max_r
                max_ans = max(max_ans, now_sum)
                # print("bac :",stack, max_ans)

                if stack[-1][1] == c_range[1] :
                    break
                
                # 裁前面
                _1 = stack[0][1]
                _2 = c_range[1]-k
                new_00 = min(stack[0][1], c_range[1]-k)
                now_sum -= (new_00-stack[0][0])*stack[0][2]
                # print("min",stack, max_ans)
                stack[0][0] = new_00
                if len(stack) == 1 :
                    # fast forward itself
                    stack[0] = [c_range[1]-k,c_range[1],c_range[2]]
                    now_sum = k*c_range[2]
                if stack[0][0] == stack[0][1] :
                    stack.popleft()
        return max_ans

# given ans

s = Solution()
# print("ans :",s.maximumCoins(coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4)) # 10
print("ans :",s.maximumCoins(coins = [[1,10,3]], k = 2)) # 6
# print("ans :",s.maximumCoins(coins = [[8,12,13],[29,32,2],[13,15,2],[40,41,18],[42,48,18],[33,36,11],[37,38,6]], k = 28)) # 226
# print("ans :",s.maximumCoins(coins = [[6,9,10],[10,14,7],[17,20,8],[23,30,12],[31,33,18],[34,40,8],[41,42,7],[45,49,18]], k = 16)) # 



