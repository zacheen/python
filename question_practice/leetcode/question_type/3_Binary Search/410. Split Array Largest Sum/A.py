# my 看 given ans (binary search) 觀念自己實作
# Runtime: 32 ms, faster than 98.13% of Python3
class Solution:
    def splitArray(self, nums, m):
        def break_group(max_sum):
            group_count = 1  # 因為最後一組也算
            now_sum = 0
            for each_num in nums :
                # 為什麼 given ans 不用這個判斷  
                # 我原本是用 left = 0 如果用 left = max(nums) 就不用
                # if each_num > max_sum :
                #     return len(nums)+1
                now_sum += each_num
                if now_sum > max_sum :
                    now_sum = each_num
                    group_count += 1
            # print("group_count :",group_count, max_sum)
            return group_count  
                    
        right = sum(nums)
        left = max(nums) # 如果是用max(nums) 而不是0 就可以註解 上面的 if each_num > max_sum :
        while left+1 < right:
            # print(left , right)
            mid = (left + right) // 2 # 曾經看到 mid = l + (r - l) // 2 竟然就不用判斷下面的 nums[left] == target ??
            # print(left, mid, " : ", nums[left], nums[mid])
            if break_group(mid) <= m :
                right = mid
            else:
                left = mid

        if break_group(left) <= m :
            # print("left")
            return left
        else :
            # print("right")
            return right

# given ans (binary search)
# 用有可能的總和 去 binary search
# 假設現在 假設的總和為 x
# 那我就從頭計算 各組總和不超過x 最後結果為幾組
# class Solution:
#     def splitArray(self, nums, m):
#         l = max(nums)
#         r = sum(nums) + 1

#         def numGroups(maxSumInGroup):
#             groupCount = 1
#             sumInGroup = 0

#             for num in nums:
#                 if sumInGroup + num <= maxSumInGroup:
#                     sumInGroup += num
#                 else:
#                     groupCount += 1
#                     sumInGroup = num
#             print("groupCount :",groupCount, maxSumInGroup)
#             return groupCount

#         while l < r:
#             mid = (l + r) // 2
#             print(l, mid, r , numGroups(mid), m)
#             if numGroups(mid) > m:
#                 l = mid + 1
#             else:
#                 r = mid

#         return l

# my (DP) Time Limit Exceeded
# 我有 cache 了 還超出時間??
# from itertools import accumulate
# import math
# class Solution:
#     def splitArray(self, nums, m):
#         # corner case
#         if len(nums) <= m :
#             return max(nums)
        
#         # 製作從頭到各自位置的總和
#         each_place_sum = []
#         now_sum = 0
#         for i in nums:
#             now_sum += i
#             each_place_sum.append(now_sum)

#         prefix = [0] + list(accumulate(nums))
#         # print(each_place_sum)
#         # print(prefix)
        
#         # 從後面往前
#         # @lru_cache(None)
#         def min_slice_k(now_place, can_slice):
#             # print(now_place, can_slice)
#             if can_slice == 0 :
#                 return each_place_sum[now_place]

#             min_comb = math.inf
#             for next_cut in range(can_slice-1, now_place) : # 我想說每段最多一個數字
#                 # print("in for :", next_cut, now_place, can_slice, each_place_sum[now_place] - each_place_sum[next_cut]) 
#                 # 多分割一段的總和是多少 each_place_sum[now_place] - each_place_sum[next_cut]) 
#                 # 新的最大總和 = max(再分割成這幾段之前最小的總和, 多分割這一段的總和)
#                 # 找最好的組合回傳 = min(這些總和)
#                 min_comb = min( min_comb , max(min_slice_k(next_cut,can_slice-1) , each_place_sum[now_place] - each_place_sum[next_cut]) )
#             # print("min_comb : ",min_comb)
#             return min_comb
        
#         return min_slice_k(len(nums)-1,m-1)


# given ans (DP)
# ... given ans 也 Time Limit Exceeded
# class Solution:
#     def splitArray(self, nums, m):
#         n = len(nums)
#         prefix = [0] + list(accumulate(nums))
        # 因為 for j in range(k - 1, i):  所以for的起始點跟k有關 
        # 又跟prefix的index base有關  因為 k - 1 要可以到第一個項目

#         # dp(i, k) := min of largest sum to split first i nums into k groups
#         # @lru_cache(None)
#         def dp(i: int, k: int):
#             if k == 1:
#                 return prefix[i]

#             ans = math.inf
#             # try all possible partitions
#             for j in range(k - 1, i):
#                 ans = min(ans, max(dp(j, k - 1), prefix[i] - prefix[j]))
#             return ans

#         return dp(n, m)

s = Solution()
# print(s.splitArray(nums = [7,2,5,10,8], m = 2))  # 18
# print(s.splitArray(nums = [1,2,3,4,5], m = 2))   # 9
# print(s.splitArray(nums = [1,4,4,4,4], m = 3))        # 4
# print(s.splitArray(nums = [1,4,4,4,4], m = 3))        # 4
# print(s.splitArray(nums = [1,4,4], m = 2))        # 4

print(s.splitArray(nums = [0,100,0,200,0], m = 2))
