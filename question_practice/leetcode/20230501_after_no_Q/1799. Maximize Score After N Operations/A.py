# 1799. Maximize Score After N Operations
# https://leetcode.com/problems/maximize-score-after-n-operations/

from typing import List
import functools

# # my v1 錯誤 (當最大公因數會出問題)
# from math import gcd
# import heapq
# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         # 計算出全部最大公因數的組合 從最大的開始拿
#             # 但我無法證明
#         gcd_list = [(-gcd(nums[i], nums[j]), nums[i], nums[j]) for i in range(len(nums)) for j in range(i)]
#         heapq.heapify(gcd_list)
#         # print(gcd_list)
        
#         count = len(nums)//2
#         ans = 0
#         while count != 0 :
#             score, n1, n2 = heapq.heappop(gcd_list)
#             if n1 == n2 :
#                 if nums.count(n1) < 2 :
#                     continue
#             else :
#                 if n1 not in nums or n2 not in nums :
#                     continue
            
#             nums.remove(n1)
#             nums.remove(n2)
#             print(score, n1, n2)
#             ans += count*score
#             count -= 1
        
#         return -ans

# # my v1 錯誤 (當最大公因數會出問題)
# from math import gcd
# import heapq
# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         # 計算出全部最大公因數的組合 從最大的開始拿
#             # 但我無法證明
#         # 最大的開始拿 + DFS 
#             # 我算 worst case 的 order 超出 time limit
              # 不知道要怎麼mem
    
# given ans # 翻譯的 Beats 14.26%
# 真正走過了每個 path, 只是 dp 了 如果剩下這些點最高的 score 是多少
# https://zxi.mytechroad.com/blog/dynamic-programming/leetcode-1799-maximize-score-after-n-operations/
    # 第二種方法的時間複雜度 不是跟第一種方法一樣嗎?
     # 都是先決定第一個點 在決定第二個點
        # 總共的 order : O(n^2*2^n) 2個for迴圈 * 共幾次 recursive(2^n 是最底層的擴散數量)
            # == 14! / 7!
        # 因為第一種方式會計算到重覆的項目
            # 像是 (1,5), (2,4), (3,6) 跟 (2,4), (1,5), (3,6) 其實結果是一樣的
            # 所以應該是 14! / 7! = 17297280 = 10^7 在 time order 內
from math import gcd
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        mem = {}

        # state 用來記錄 現在哪些位置已經走過了
        count_time = 0
        def dfs(round , state) :
            nonlocal count_time
            if round > (len(nums) >> 1) :
                return 0
            if state in mem.keys() :
                return mem[state]
            
            ans = 0
            for i in range(len(nums)) :
                for j in range(0, i) :
                    count_time += 1
                    picked = 1 << i | 1 << j 
                    # 當 state i 跟 j 的位置為 0，& 的結果才會為 0
                    if (state & picked) == 0 :
                        ans = max(ans, \
                            round*gcd(nums[i], nums[j]) + dfs(round + 1, state | picked ))
                            # 本次連結分數              + 其他連結分數  "state | picked" 用來記錄目前走過的 index 
            mem[state] = ans
            return ans

        ret = dfs(1, 0)
        print("count_time : ",count_time)
        return ret

s = Solution()
print(s.maxScore(nums = [3,4,6,8]))
print(s.maxScore(nums = [1,2,3,4,5,6]))
print(s.maxScore(nums = [415,230,471,705,902,87]))



