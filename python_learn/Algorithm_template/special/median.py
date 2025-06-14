# trace median in O(logn)

# classic problem
    # 480. Sliding Window Median
    # https://leetcode.com/problems/sliding-window-median/description/
        # 需要增加，也需要減少
            # Median_twoHeap    : 87ms  Beats84.75%
            # Median_SortedList : 237ms Beats39.75%
    # 295. Find Median from Data Stream
    # https://leetcode.com/problems/find-median-from-data-stream/
        # 從沒有項目開始，且只會增加，有點不准
            # Median_SortedList      : 229ms
            # Median_twoHeap_onlyAdd : 125ms
            # Median_2SortedList     : 356ms

from heapq import heappush, heappop, heapify
from collections import Counter
# 最快
class Median_twoHeap:
    def __init__(self, nums):
        nums.sort()
        self.small = [-n for n in nums[:len(nums)//2]]
        heapify(self.small)
        self.big = nums[len(nums)//2:]
        heapify(self.big)
        self.bal = len(self.big)-len(self.small) # 看 big 比 small 多多少
        self.removals = Counter()

    def balance(self):
        while self.bal > 1:
            heappush(self.small, -heappop(self.big))
            self.bal -= 2
        while self.bal < 0:
            heappush(self.big, -heappop(self.small))
            self.bal += 2

        # 因為我 remove 的時候預設是放到 self.big 裡面，所以要先扣 self.big 的
        while self.big and self.removals[self.big[0]]:
            self.removals[self.big[0]] -= 1
            heappop(self.big)
        
        while self.small and self.removals[-self.small[0]]:
            self.removals[-self.small[0]] -= 1
            heappop(self.small)

    def add(self, num):
        if self.big and num >= self.big[0] :
            self.bal += 1
            heappush(self.big, num)
        else:
            self.bal -= 1
            heappush(self.small, -num)
                
    def remove(self, num):
        self.removals[num] += 1
        if num >= self.big[0] :
            self.bal -= 1
        else :
            self.bal += 1
    
    # 找中位數
    def get_median(self):
        self.balance()
        if self.bal :
            return self.big[0]
        else :
            return (self.big[0] - self.small[0])/2

from sortedcontainers import SortedList
# 最通用
class Median_SortedList:
    def __init__(self, nums):
        self.nums = SortedList(nums)

    def update_mid_i(self):
        self.med_i = len(self.nums)//2
        self.med_e_i = self.med_i-1
        self.odd_f = len(self.nums)&1

    def get_median(self):
        self.update_mid_i()
        if self.odd_f :
            return self.nums[self.med_i]
        else :
            return (self.nums[self.med_e_i] + self.nums[self.med_i])/2
    
    def add(self, add_n):
        self.nums.add(add_n)

    def remove(self, remove_n):
        self.nums.remove(remove_n)

from heapq import heappush, heappushpop
# 如果項目只會增加，用這個比較快
class Median_twoHeap_onlyAdd:
    def __init__(self):
        self.big = []
        self.small = []

    def add(self, num):
        if len(self.big) > len(self.small) :
            # need to put into big
            if self.big and num > self.big[0] :
                num = heappushpop(self.big, num)
            heappush(self.small, -num)
        else :
            # need to put into small
            if self.small and num < -self.small[0] :
                num = -heappushpop(self.small, -num)
            heappush(self.big, num)

    # 找中間的數字(如果是偶數個 就取小的那個)
    def findmid(self):
        return self.big[0]
    
    # 找中位數
    def findMedian(self):
        if len(self.big) == len(self.small) :
            return (self.big[0] - self.small[0])/2
        else :
            return self.big[0]

# 可以增加，也可以減少項目
    # 如果需要兩邊的資料，可能這個比較好處理 (但基本不會用到...)
# class Median_2SortedList:
#     def __init__(self, nums):
#         nums.sort()
#         # med_i = len(nums)//2
#         med_end = (len(nums)+1)//2
#         self.fro_l = SortedList(nums[:med_end])
#         self.bac_l = SortedList(nums[med_end:])

#     def get_median(self):
#         if len(self.fro_l) == len(self.bac_l) :
#             return (self.fro_l[-1] + self.bac_l[0])/2
#         else :
#             return self.fro_l[-1]
    
#     # fro_l 的數量一定 1. 等於bac_l 2. 多bac_l一個
#         # 所以 fro_l[-1] 一定是 median
#     def balance(self):
#         if len(self.fro_l) > len(self.bac_l) + 1 :
#             self.bac_l.add(self.fro_l.pop(-1))
#         elif len(self.bac_l) > len(self.fro_l):
#             self.fro_l.add(self.bac_l.pop(0))
    
#     def addNum(self, add_n):
#         if not self.fro_l or add_n <= self.fro_l[-1] :
#             self.fro_l.add(add_n)
#         else :
#             self.bac_l.add(add_n)
#         self.balance()

#     def remove(self, remove_n):
#         if remove_n <= self.fro_l[-1] :
#             self.fro_l.remove(remove_n)
#         else :
#             self.bac_l.remove(remove_n)
#         self.balance()

# # 優化失敗 ####################################################
# from heapq import heappop, heappush
# from collections import Counter
# class Median_twoHeap:
#     def __init__(self, nums):
#         nums.sort()
#         self.small = nums[:len(self.nums)//2+1]
#         self.big = nums[len(self.nums)//2+1:]
#         # # 優化失敗
#         # self.small = []
#         # self.big = nums.copy()
#         # heapify(self.big)
#         # while len(self.small) < len(self.big):
#         #     heappush(self.small, -heappop(self.big))
#         self.bal = len(self.big)-len(self.small) # 看 big 比 small 多多少
#         self.removals = Counter()
#         self.balance = 0 # 看 big 比 small 多多少

#     def balance(self):
#         while self.balance < 0:
#             heappush(self.small, -heappop(self.big))
#         while self.balance > 0:
#             heappush(self.big, -heappop(self.small))

#         # 優化失敗
#         # # 在這裡也判斷一次 pop_num 是否需要被移除
#         # while self.balance < 0:
#         #     pop_num = heappop(self.big)
#         #     if self.removals[pop_num] > 0:
#         #         self.removals[pop_num] -= 1
#         #     else :
#         #         heappush(self.small, -pop_num)
#         # while self.balance > 0:
#         #     pop_num = -heappop(self.small)
#         #     if self.removals[pop_num] > 0:
#         #         self.removals[pop_num] -= 1
#         #     else :
#         #         heappush(self.big, pop_num)

#         while self.small and self.removals[-self.small[0]]:
#             self.removals[-self.small[0]] -= 1
#             heappop(self.small)

#         while self.big and self.removals[self.big[0]]:
#             self.removals[self.big[0]] -= 1
#             heappop(self.big)

#     def add(self, num):
#         if self.big and num >= self.big[0] :
#             self.balance += 1
#             heappush(self.big, num)
#         else:
#             self.balance -= 1
#             heappush(self.small, -num)
                
#     def remove(self, num):
#         self.removals[num] += 1
#         if num >= self.big[0] :
#             self.balance -= 1
#         else :
#             self.balance += 1
    
#     # 找中位數
#     def findMedian(self):
#         if len(self.small) == len(self.big) :
#             return (self.big[0] - self.small[0])/2
#         else :
#             return self.big[0]