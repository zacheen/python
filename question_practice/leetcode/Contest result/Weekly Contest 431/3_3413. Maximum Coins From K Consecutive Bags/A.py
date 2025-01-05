# 3413. Maximum Coins From K Consecutive Bags
# https://leetcode.com/problems/maximum-coins-from-k-consecutive-bags/description/

from typing import List
import functools

from collections import deque

# my 742ms Beats100.00% O(2n) (for coins)+(pop stack)
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

import bisect
from itertools import accumulate
# No.1 ans, after my opt 679ms Beats100.00%
# directly gather all possible l, and directly cal the sum
# but why it is faster? O(nlogn) (for candidate_L) * (bisect_left)
class Solution:
    def maximumCoins(self, coins: List[List[int]], k: int) -> int:
        # Step 1: Sort the segments based on start positions
        coins_sorted = sorted(coins, key=lambda x: x[0])
        n = len(coins_sorted)
        
        # Extract start positions, end positions, and coin values
        starts = [segment[0] for segment in coins_sorted]
        ends = [segment[1] for segment in coins_sorted]
        coin_values = [segment[2] for segment in coins_sorted]
        
        # Step 2: Compute prefix sums of total coins up to each segment
        prefix_sum = list(
            accumulate( (ends-starts+1)*coin_values for starts, ends, coin_values in coins_sorted )
        )

        # Step 3: Collect all candidate window start positions: li's and ri -k +1's
        candidate_L = set()
        for seg in coins_sorted:
            candidate_L.add(seg[0])
            adjusted_L = seg[1] - k + 1
            if adjusted_L >= 1:
                candidate_L.add(adjusted_L)
        candidate_L = sorted(candidate_L)
        
        max_coins = 0
        
        for L in candidate_L:
            R = L + k -1
            # Find the first segment with ri >= L
            left_idx = bisect.bisect_left(ends, L)
            # Find the last segment with li <= R
            right_idx = bisect.bisect_right(starts, R) -1
            if left_idx > right_idx or left_idx == n:
                # No overlapping segments
                current_sum = 0
            else:
                # Total coins from left_idx to right_idx
                total = prefix_sum[right_idx]
                if left_idx > 0:
                    total -= prefix_sum[left_idx -1]
                
                # Adjust for partial overlap at the start
                if starts[left_idx] < L:
                    overlap_length = L - starts[left_idx]
                    total -= overlap_length * coin_values[left_idx]
                
                # Adjust for partial overlap at the end
                if ends[right_idx] > R:
                    overlap_length = ends[right_idx] - R
                    total -= overlap_length * coin_values[right_idx]
                
                current_sum = total
            
            if current_sum > max_coins:
                max_coins = current_sum
        
        return max_coins
    
#given ans
# do fron front only deal cutting front, and reverse do it again backward

s = Solution()
print("ans :",s.maximumCoins(coins = [[8,10,1],[1,3,2],[5,6,4]], k = 4)) # 10
print("ans :",s.maximumCoins(coins = [[1,10,3]], k = 2)) # 6
print("ans :",s.maximumCoins(coins = [[8,12,13],[29,32,2],[13,15,2],[40,41,18],[42,48,18],[33,36,11],[37,38,6]], k = 28)) # 226
print("ans :",s.maximumCoins(coins = [[6,9,10],[10,14,7],[17,20,8],[23,30,12],[31,33,18],[34,40,8],[41,42,7],[45,49,18]], k = 16)) # 190



