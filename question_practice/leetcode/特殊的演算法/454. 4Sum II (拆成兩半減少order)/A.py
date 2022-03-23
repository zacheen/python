# My Time Limit Exceeded
# ans_count = 0
# class Solution:
#     def fourSumCount(self, nums1 , nums2 , nums3 , nums4 ):
#         global ans_count
#         ans_count = 0
#         def rec(now_sum, n):
#             global ans_count
#             # print(now_sum, n)
#             if n==5 :
#                 if now_sum == 0 :
#                     ans_count = ans_count + 1
#                 return
#             elif n == 4 :
#                 for each_num in nums4 :
#                     rec(now_sum + each_num, 5)
#             elif n == 3 :
#                 for each_num in nums3 :
#                     rec(now_sum + each_num, 4)
#             elif n == 2 :
#                 for each_num in nums2 :
#                     rec(now_sum + each_num, 3)
#             else :
#                 for each_num in nums1 :
#                     rec(now_sum + each_num, 2)
            
#         rec(0, 1)

#         return ans_count

# # My v2 先count   時間還是超過...   
# # Time Limit Exceeded  
# from collections import Counter

# ans_count = 0
# class Solution:
#     def fourSumCount(self, nums1 , nums2 , nums3 , nums4 ):
#         global ans_count
#         ans_count = 0

#         count_num = []
#         count_num.append(Counter(nums1))
#         count_num.append(Counter(nums2))
#         count_num.append(Counter(nums3))
#         count_num.append(Counter(nums4))

#         def rec(now_sum, n, mul):
#             global ans_count
#             print(now_sum, n)
#             if n==4 :
#                 if now_sum == 0 :
#                     ans_count = ans_count + mul
#                 return
#             for each_num, each_count in count_num[n].items() :
#                 rec(now_sum + each_num, n+1, each_count*mul)
            
#         rec(0, 0, 1) # base 跟上面不一樣

#         return ans_count

# My v3 先count 第四個用 hash  
# Time Limit Exceeded ...
# from collections import Counter

# ans_count = 0
# class Solution:
#     def fourSumCount(self, nums1 , nums2 , nums3 , nums4 ):
#         global ans_count
#         ans_count = 0

#         count_num = []
#         count_num.append(Counter(nums1))
#         count_num.append(Counter(nums2))
#         count_num.append(Counter(nums3))
#         count_num4 = Counter(nums4)

#         def rec(now_sum, n, mul):
#             global ans_count
#             # print(now_sum, n)
#             if n==3 :
#                 ans_count += count_num4[-now_sum]*mul
#                 return
#             for each_num, each_count in count_num[n].items() :
#                 rec(now_sum + each_num, n+1, each_count*mul)
            
#         rec(0, 0, 1)

#         return ans_count

# given ans
# 邏輯 不只 hash 還拆成兩半
from collections import Counter
class Solution:
    def fourSumCount(self, A, B, C, D):
        count = Counter(a + b for a in A for b in B)
        return sum(count[-c - d] for c in C for d in D)

s = Solution()
print(s.fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
print(s.fourSumCount([0],[0],[0],[0]))

