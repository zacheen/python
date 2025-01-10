# 2762. Continuous Subarrays
# https://leetcode.com/problems/continuous-subarrays/description

from typing import List
import functools

# # my Time Limit Exceeded
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         ans_cou = len(nums)
#         for l, l_n  in enumerate(nums) :
#             max_n = l_n
#             min_n = l_n
#             for r_n in nums[l+1: len(nums)] :
#                 max_n = max(max_n, r_n)
#                 min_n = min(min_n, r_n)
#                 if max_n - min_n <= 2 :
#                     ans_cou+=1
#                 else :
#                     break
#         return ans_cou

# # given ans 611ms Beats77.49% 
# from collections import deque
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         # Monotonic deque to track maximum and minimum elements
#         max_q = deque() # 紀錄現在數字最大的 indx 位置
#         min_q = deque()
#         left = 0
#         count = 0

#         for right, num in enumerate(nums):
#             # 因為是紀錄最大的位置，因此遇到較小的剔除
#             while max_q and nums[max_q[-1]] < num:
#                 max_q.pop()
#             max_q.append(right)
#             print("max_q",max_q)

#             # Maintain increasing monotonic deque for minimum values
#             while min_q and nums[min_q[-1]] > num:
#                 min_q.pop()
#             min_q.append(right)
#             print("min_q",min_q)

#             # Shrink window if max-min difference exceeds 2
#             while max_q and min_q and nums[max_q[0]] - nums[min_q[0]] > 2:
#                 # Move left pointer past the element that breaks the condition
#                 print(max_q[0], min_q[0])
#                 if max_q[0] < min_q[0]:
#                     left = max_q[0] + 1
#                     max_q.popleft()
#                 else:
#                     left = min_q[0] + 1
#                     min_q.popleft()
#                 print("max_q",max_q)
#                 print("min_q",min_q)
#             # Add count of all valid subarrays ending at current right pointer
#             count += right - left + 1

#         return count

# # my opt v2 581ms Beats94.74%
from collections import deque
class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        ans_count = 0
        l = -1
        max_indx = deque() # descend order
        min_indx = deque() # increase order
        for r, n in enumerate(nums) :
            while max_indx and n > nums[max_indx[-1]] :
                max_indx.pop()
            max_indx.append(r)
            while min_indx and n < nums[min_indx[-1]] :
                min_indx.pop()
            min_indx.append(r)
            # 如果最大的 - 最小的 不符合條件
            while nums[max_indx[0]] - nums[min_indx[0]] > 2 :
                # 比較哪個indx比較遠，較遠的先pop
                if max_indx[0] < min_indx[0] :
                    l = max_indx.popleft()
                else :
                    l = min_indx.popleft()
            ans_count += r - l
        return ans_count
    
# # my opt v1 slower 較好理解
# from collections import deque
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         ans_count = 0
#         l = 0
#         max_indx = deque() # descend order
#         min_indx = deque() # increase order
#         for r, n in enumerate(nums) :
#             while max_indx and n > max_indx[-1][1] :
#                 max_indx.pop()
#             max_indx.append((r,n))
#             while min_indx and n < min_indx[-1][1] :
#                 min_indx.pop()
#             min_indx.append((r,n))

#             # print(max_indx, min_indx)
#             # 如果最大的 - 最小的 不符合條件
#             while max_indx[0][1] -  min_indx[0][1] > 2 :
#                 # 比較哪個indx比較遠，較遠的先pop
#                 if max_indx[0][0] < min_indx[0][0] :
#                     # 排除掉這一個的下一個是可以包含的
#                     l = max_indx.popleft()[0] + 1
#                 else :
#                     l = min_indx.popleft()[0] + 1
            
#             # print(l, r)
#             ans_count += r - l + 1
#         return ans_count

# # given ans 840ms Beats20.76%
# # require maintaining two heap, slower but more general
# import heapq    
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         # Two heaps to track min/max indices, sorted by nums[index]
#         min_heap = []  # (nums[i], i) tuples for min tracking
#         max_heap = []  # (-nums[i], i) tuples for max tracking
#         left = right = 0
#         count = 0

#         while right < len(nums):
#             # Add current index to both heaps
#             # For max heap, negate value to convert min heap to max heap
#             heapq.heappush(min_heap, (nums[right], right))
#             heapq.heappush(max_heap, (-nums[right], right))

#             # While window violates |nums[i] - nums[j]| ≤ 2
#             # Shrink window from left and remove outdated indices
#             while left < right and -max_heap[0][0] - min_heap[0][0] > 2:
#                 left += 1

#                 # Remove indices outside window from both heaps
#                 while min_heap and min_heap[0][1] < left:
#                     heapq.heappop(min_heap)
#                 while max_heap and max_heap[0][1] < left:
#                     heapq.heappop(max_heap)

#             count += right - left + 1
#             right += 1

#         return count

# # given ans
# # this method works because in max(freq) - min(freq) freq only contain maximum 4 keys
# class Solution:
#     def continuousSubarrays(self, nums: List[int]) -> int:
#         # Map to maintain sorted frequency map of current window
#         freq = {}
#         left = right = 0
#         count = 0  # Total count of valid subarrays

#         while right < len(nums):
#             # Add current element to frequency map
#             freq[nums[right]] = freq.get(nums[right], 0) + 1

#             # While window violates the condition |nums[i] - nums[j]| ≤ 2
#             # Shrink window from left
#             while max(freq) - min(freq) > 2:
#                 # Remove leftmost element from frequency map
#                 freq[nums[left]] -= 1
#                 if freq[nums[left]] == 0:
#                     del freq[nums[left]]
#                 left += 1

#             # Add count of all valid subarrays ending at right
#             count += right - left + 1
#             right += 1

#         return count

s = Solution()
# print("ans :",s.continuousSubarrays(nums = [5,4,2,4])) # 8
# print("ans :",s.continuousSubarrays(nums = [1,2,3])) # 6
print("ans :",s.continuousSubarrays(nums = [31,30,31,32])) # 10



