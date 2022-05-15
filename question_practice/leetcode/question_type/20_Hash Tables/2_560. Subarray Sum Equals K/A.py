from collections import defaultdict
import bisect 
# my Runtime: 397 ms, faster than 26.65% of Python3
# class Solution:
#     def subarraySum(self, nums, k):
#         # 從第一個到某個 中間 從某個到最後一個
#         total = sum(nums)
#         remain_sum = total - k
        
#         # notice that in the list is end of the pos(not include)
#         posible = defaultdict(list)
#         now_total = 0
#         # notice that didnt record all sum into it
#         for indx, n in enumerate(nums) :
#             posible[now_total].append(indx)
#             now_total += n
            
#         ans = 0
#         now_total = 0
#         for indx in range(len(nums)-1, -1, -1) :
#             # (O)
#             ans += bisect.bisect_right(posible[remain_sum - now_total], indx)
#             # for pos_indx in posible[remain_sum - now_total] :
#             #     if pos_indx <= indx :
#             #         ans += 1
#             #     else :
#             #         break
#             now_total += nums[indx]
#         return ans
            
# 這個是 如果全部都是正的 才會正常運作
#         now_total = 0
#         l,r = 0,0
#         ans = 0
#         while r < len(nums) :
#             now_total += nums[r]
#             r += 1
            
#             while now_total >= k and l < r :
#                 if now_total == k :
#                     ans += 1
                    
#                 now_total -= nums[l]
#                 l += 1
#         return ans        


# given ans
from collections import Counter
# 計算從頭到現在有幾種總和
# 計算 [總和 - k = 前面的總和] 有幾種加總方式
class Solution:
    def subarraySum(self, nums, k):
        ans = 0
        prefix = 0
        count = Counter({0: 1})

        for num in nums:
            prefix += num
            ans += count[prefix - k]
            count[prefix] += 1

        return ans

s = Solution()
print(s.subarraySum([1,1,1],2))
print(s.subarraySum([3,2,1],3))
print(s.subarraySum([-1,-1,1],0))



