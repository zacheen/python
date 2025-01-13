# 3420. Count Non-Decreasing Subarrays After K Operations
# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/description/

from typing import List
import functools

# given ans 260ms Beats100.00%
# 1. 為什麼要倒過來做 > 因為這樣才會知道有哪些數字受到此數的影響
    # 5234 我並不知道 4 後面的數字會不會受影響
    # 但我反過來做 4325 到 5 的時候我知道所有受到影響的數字
from collections import deque
class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        nums = nums[::-1]
        # print(nums)
        ans = 0
        q = deque() # saving the number that is bigger (always in decrease order)
        l_i = 0 # l_i : 目前可以的 indx 最左邊
        for r_i, now_r in enumerate(nums): # r_i : 目前可以的 indx 最右邊
            while q and nums[q[-1]] < now_r: # now_r 比最後最大的數字更大
                last_b_i = q.pop() # last_b_i : 前一個最大的數字的 indx
                least_q_i = q[-1] if q else l_i - 1 # least_q_i : 最小會被影響的數字的 indx
                k -= (last_b_i - least_q_i) * (now_r - nums[last_b_i]) # 有幾個數字受影響 * 這個數字到前一個數字影響多少
            q.append(r_i)
            while k < 0:
                k += nums[q[0]] - nums[l_i] # recover
                if q[0] == l_i:
                    q.popleft()
                l_i += 1
            ans += (r_i - l_i) + 1 # 植樹+1 #把 r_i 可以的組合加到 ans
        return ans

s = Solution()
# print("ans :",s.countNonDecreasingSubarrays(nums = [6,3,1,2,4,4], k = 7)) # 17
# print("ans :",s.countNonDecreasingSubarrays(nums = [6,3,1,3,6], k = 4)) # 12
# print("ans :",s.countNonDecreasingSubarrays([10,16,11,16],3)) # 6
# print("ans :",s.countNonDecreasingSubarrays([5,2,3,4],4)) # 6
print("ans :",s.countNonDecreasingSubarrays([6,5,4,5,4,5,4],6)) # 6



