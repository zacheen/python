# my Runtime: 151 ms, faster than 86.33% of Python3
# 我覺得這個情況應該是 list 比較快
# 因為 刪除是 O(log n) 如果是heap是O(n) 
from bisect import bisect_left
from bisect import insort_right
class Solution:
    def medianSlidingWindow(self, nums, k):
        now_list = nums[:k]
        now_list.sort()
        
        is_even = (k % 2) == 0
        mid_indx = (k // 2)
        mid_even_indx = mid_indx-1
        def get_medi():
            if is_even :
                return (now_list[mid_even_indx] + now_list[mid_indx])/2
            else :
                return now_list[mid_indx]
                
        ans = []
        ans.append(get_medi())
        for i, next_num in enumerate(nums[k:]):
            rm_idx = bisect_left(now_list, nums[i])
            del(now_list[rm_idx])
            insort_right(now_list, next_num)
            ans.append(get_medi())
        return ans

# my (two heap version)
# 的確比較慢
# Runtime: 335 ms, faster than 46.60% of Python3 
# 概念跟題目 295 一樣
# 只是要自己實作 remove
# import heapq
# class Solution:
#     def medianSlidingWindow(self, nums, k):
#         maxHeap = []
#         minHeap = []

#         def balance():
#             # balance two heaps s.t.
#             if len(maxHeap) < len(minHeap):
#                 heapq.heappush(maxHeap, -heapq.heappop(minHeap))
#             elif len(maxHeap) - len(minHeap) > 1:
#                 heapq.heappush(minHeap, -heapq.heappop(maxHeap))

#         def addNum(num):
#             if not maxHeap or num <= -maxHeap[0]:
#                 heapq.heappush(maxHeap, -num)
#             else:
#                 heapq.heappush(minHeap, num)
#             balance()

#         def remove_num(value):
#             # print("in remove_num :", minHeap, maxHeap)
#             if value <= -maxHeap[0] :
#                 rm_indx = maxHeap.index(-value)
#                 remove_from_num(maxHeap, rm_indx)
#             else :
#                 rm_indx = minHeap.index(value)
#                 remove_from_num(minHeap, rm_indx)
#             balance()
        
#         def remove_from_num(h, rm_indx):
#             h[rm_indx] = h[-1]
#             h.pop()
#             if rm_indx < len(h):
#                 heapq._siftup(h, rm_indx)
#                 heapq._siftdown(h, 0, rm_indx)

#         is_even = (k % 2) == 0
#         def get_medi():
#             if is_even:
#                 # print(minHeap, maxHeap, (-maxHeap[0] + minHeap[0]) / 2.0)
#                 return (-maxHeap[0] + minHeap[0]) / 2.0
#             return -maxHeap[0]

#         for num in nums[:k]:
#             addNum(num)

#         ans = []
#         ans.append(get_medi())
#         for i, next_num in enumerate(nums[k:]):
#             remove_num(nums[i])
#             addNum(next_num)
#             ans.append(get_medi())
#         return ans

# given ans

s = Solution()
print(s.medianSlidingWindow([1,3,-1,-3,5,3,6,7],4))



