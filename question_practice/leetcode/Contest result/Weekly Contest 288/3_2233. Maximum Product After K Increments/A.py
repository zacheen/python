# my Runtime: 2307 ms, faster than 10.00% of Python3
# 我以為最後的結果才會 > 1000000007  
# 所以在 time out of limit 卡了一下
# 優化 submit 了很多次
# 時間複雜度 O(log(max_num))*n)
# class Solution:
#     def maximumProduct(self, nums, k):
#         # 我要找最大的數字 讓條件可以符合條件k
#         left, right = min(nums), max(nums) + k + 1
        
#         while left + 1 < right:
#             # print(left, right)
#             mid = (left + right) // 2
#             # 計算k是否能符合
#             s = 0
#             for n in nums :
#                 s += max(mid-n, 0)
#                 if s > k :
#                     break
            
#             # print(mid, s)
#             if s > k :
#                 right = mid
#             else :
#                 left = mid
              
#         # print(left, right)
#         # left 是一定可以的  所以全部先換成 left
#         for i in range(len(nums)) :
#             if nums[i] < left :
#                 k -= (left -nums[i])
#                 nums[i] = left
#         # 如果 k 還有剩再換成 right
#         if k != 0 :
#             for i in range(len(nums)) :
#                 if nums[i] == left :
#                     k -= 1
#                     nums[i] = right
#                     if k == 0 :
#                         break
                        
#         ans = 1
#         for i in nums :
#             ans *= i
#             ans = ans % 1000000007
#             # 靠腰 這裡太大了 算很慢啦
#         return ans

# my v1 time out of limit
# class Solution:
#     def maximumProduct(self, nums, k):
#         min_num = min(nums)
#         while True :
#             for i, n in enumerate(nums) :
#                 if n == min_num :
#                     nums[i] += 1
#                     k -= 1
#                     if k == 0 :
#                         ans = 1
#                         for i in nums :
#                             ans *= i
#                         return ans % 1000000007
#             min_num += 1

# given ans
# 大家竟然都用 heap 每次取最大的++
# (也許因為是coding最快的方法)
# 時間複雜度 O(log(n)*k)
    # 按 Constraints 來算 好像他的比較快
    # 1 <= nums.length, k <= 10^5
    # 0 <= nums[i] <= 10^6
# 也沒有超過 time limit

# 看完 given ans 自己實作看看
# Runtime: 2341 ms, faster than 10.00% of Python3
# 跟 binary sort 所花的時間差不多啦
class Solution:
    def maximumProduct(self, nums, k):
        heapq.heapify(nums)
        
        for _ in range(k) :
            min_num = heapq.heappop(nums)
            heapq.heappush(nums, min_num+1)
                        
        ans = 1
        for i in nums :
            ans *= i
            ans = ans % 1000000007
        return ans

s = Solution()
print(s.maximumProduct(nums = [0,4], k = 5))
print(s.maximumProduct(nums = [6,3,3,2], k = 2))


