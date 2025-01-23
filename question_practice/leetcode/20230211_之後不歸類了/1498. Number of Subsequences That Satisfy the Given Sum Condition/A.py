# 1498. Number of Subsequences That Satisfy the Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

from typing import List
import functools

# # my v1 Time Limit Exceeded
# class Solution:
#     def numSubseq(self, nums: List[int], target: int) -> int:
#         # 先選一個 nums 當 maximum 
#         # 再看有什麼數字可以當 minimum
#         # 然後中間就是其他可以挑選的組合
#         # 下一回合一定不包含 maximum 所以一定不會重複

#         @functools.lru_cache(None)
#         def cal_combination(n):
#             if n <= 0 :
#                 return 1
#             return cal_combination(n-1)*2

#         nums.sort()
#         ans = 0
#         for r in range(len(nums)-1,-1,-1):
#             maximum = nums[r]
#             # l 可以的位置我也可以直接找拉 # opt
#             for l in range(r+1) :
#                 if maximum + nums[l] <= target:
#                     # l~r 中間有 r-l-1 個選項 (不包含 r l , r l 一定要選)
#                     # print(l,r)
#                     ans += cal_combination(r-l-1)
#                     ans = ans % 1000000007
#                 else :
#                     break
#         return ans


# my v2 Beats 58.82%
import bisect
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        # 先選一個 nums 當 maximum 
        # 再看有什麼數字可以當 minimum
        # 然後中間就是其他可以挑選的組合
        # 下一回合一定不包含 maximum 所以一定不會重複

        @functools.lru_cache(None)
        def cal_combination(n):
            if n <= 0 :
                return 1
            return cal_combination(n-1)*2 % 1000000007
        
        # @functools.lru_cache(None) # 無法 cache 因為 r 一定不一樣
        def sum_combinations(r,max_l):
            ans = 0
            # for l in range(max_l) :
            #     # l~r 中間有 r-l-1 個選項 (不包含 r l , r l 一定要選)
            #     ans += cal_combination(r-l-1)
            #     ans = ans % 1000000007
            #=============================================================
            # # 省略 l, r-l-1 的範圍是 r-1(include) ~ r-max_l-1(not include)
            # for comb_num in range(r-max_l, r) :
            #     # l~r 中間有 r-l-1 個選項 (不包含 r l , r l 一定要選)
            #     # print("comb_num : ",comb_num)
            #     ans += cal_combination(comb_num)
            #     ans = ans % 1000000007
            # # print(r-max_l,r,"correct",ans)
            # # return ans
            #=============================================================
            if (r-max_l >= r) :
                return 0
            if r == 0 : # deal the situation when r-1 == -1
                return 1
            
            # # 2**0 + 2**1 + ... + 2**(r-1) + "r-max_l 如果是-1要加一" -> 等比級數
            add = 0
            from_num = r-max_l
            if from_num == -1:
                add = 1
                from_num = 0

            q = 2
            # ret = (2**from_num - (2**(r-1)*q))/(1-q) + add
            # ret = (cal_combination(from_num) - (cal_combination(r-1)*q)) / (1-q) + add # 這種計算方法會變成浮點數 導致數值計算錯誤
            ret = (cal_combination(from_num) - (cal_combination(r-1)*q)) // (1-q) + add
            # ret = (cal_combination(r-1)*q) - cal_combination(from_num) + add # 上面的可以再優化成這樣
            ret = int(ret) % 1000000007
            print("check", from_num, cal_combination(from_num),2**from_num,"||",  r-1, 2**(r-1), cal_combination(r-1), ans, int(ret), add)
            # if ans != ret :
            #     print("error!")
            # print(r-max_l,r,"opt",ret)
            return ret % 1000000007

        nums.sort()
        ans = 0
        for r in range(len(nums)-1,-1,-1):
            maximum = nums[r]
            max_l = bisect.bisect_right(nums, target - maximum)
            # 這下面可以用成 function
            # for l in range(0,min(max_l, r+1)) :
            #     # l~r 中間有 r-l-1 個選項 (不包含 r l , r l 一定要選)
            #     ans += cal_combination(r-l-1)
            #     ans = ans % 1000000007
            # ==
            ans += sum_combinations(r,min(max_l, r+1))
            ans = ans % 1000000007

        return ans

# given ans Beats 70.33%
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        kMod = 1_000_000_007
        n = len(nums)
        ans = 0

        nums.sort()

        l = 0
        r = n - 1
        while l <= r:
            if nums[l] + nums[r] <= target:
                # 原本我的想法是 l,r 都要包含到 # 其實可以只包含 l，這樣就會變成從 r~l的前一個的組合(共 r-l 個數字)
                ans += pow(2, r - l, kMod)
                l += 1
            else:
                r -= 1

        return ans % kMod

s = Solution()
print(s.numSubseq(nums = [3,5,6,7], target = 9))  # 4
print(s.numSubseq(nums = [3,3,6,8], target = 10)) # 6
print(s.numSubseq(nums = [2,3,3,4,6,7], target = 12)) # 61
print(s.numSubseq(nums = [1], target = 1)) # 61
# print(s.numSubseq(nums = [11,24,5,29,12,3,4,7,9,25,8,15,25,26,17,29,16,14,19,1,27,18,29,2,18,10,8,25,22,4,24,8,5,5,10,9,26,21,25,29,12,24,28,12,4,26,6,6,2,21,12,8,2,12,2,9,25,22,15,18,4,9,30,17,10,30,7,1,6,3,26,16,2,15,13,14,28,12,11,6,15,24,25,8], target = 39)) # 61



