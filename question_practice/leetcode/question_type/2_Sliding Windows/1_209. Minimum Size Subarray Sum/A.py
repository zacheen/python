# my v1 Runtime: 115 ms, faster than 43.78% of Python3
# 這裡有一個特性是數字全是正的 所以可以用 sliding window
# class Solution:
#     def minSubArrayLen(self, target, nums):
#         l,r = 0,0
#         min_len = len(nums) + 1
#         now_total = 0
#         while r < len(nums) :
#             now_total += nums[r]
#             r += 1
#             # print("in r loop :", l , r , now_total)
#             if now_total >= target :
#                 last_sum = now_total
#                 while l < r:
#                     # print("in l loop :", l , r , now_total)
#                     now_total -= nums[l]
#                     l += 1
#                     if now_total < target :
#                         break
#                     last_sum = now_total
#                 min_len = min(r - l, min_len)
                
#         if min_len == len(nums) + 1 :
#             return 0
#         else :
#             return min_len + 1

# 整理code 優化後
# Runtime: 75 ms, faster than 90.78% of Python3
class Solution:
    def minSubArrayLen(self, target, nums):
        l,r = 0,0
        min_len = len(nums) + 1
        now_total = 0
        while r < len(nums) :
            now_total += nums[r]
            r += 1
            # print("in r loop :", l , r , now_total)
            if now_total >= target:
                # 其實不用判斷 l < r 因為當 l<r 符合時 now_total < target 一定也會符合
                while l < r :
                    # print("in l loop :", l , r , now_total)
                    now_total -= nums[l]
                    l += 1
                    if now_total < target :
                        break
                min_len = min(r - l, min_len)
                
        if min_len == len(nums) + 1 :
            return 0
        else :
            return min_len + 1
            
# given ans 
# class Solution:
#     def minSubArrayLen(self, target, nums):
#         ans = math.inf
#         sum = 0
#         j = 0

#         for i, num in enumerate(nums):
#             sum += num
#             while sum >= s:
#                 ans = min(ans, i - j + 1)
#                 sum -= nums[j]
#                 j += 1

#         return ans if ans != math.inf else 0

s = Solution()
print(s.minSubArrayLen(target = 7, nums = [2,3,1,2,4,3]))
print(s.minSubArrayLen(target = 7, nums = [2,4,3,2,3,1,2,7]))
print(s.minSubArrayLen(target = 7, nums = [1,7,7]))
print(s.minSubArrayLen(target = 5, nums = [1,1,1,1,1,2,1,1,1,1,1]))
print(s.minSubArrayLen(target = 7, nums = [3,4,8]))
