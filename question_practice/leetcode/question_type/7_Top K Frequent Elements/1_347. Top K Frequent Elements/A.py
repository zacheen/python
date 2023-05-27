from collections import Counter
# my Runtime: 107 ms, faster than 86.33% of Python3
class Solution:
    def topKFrequent(self, nums, k):
        return [i[0] for i in Counter(nums).most_common(k)]

# # 20230522 重新練習 Beats 43.78% (較慢)
# 如果是 Counter 可以呼叫 most_common 替代(底層也是呼叫 nlargest)
# import heapq
# class Solution:
#     def topKFrequent(self, nums, k):
#         count = [ (c, n) for n, c in Counter(nums).items() ]
#         return [n for _, n in heapq.nlargest(k, count)]

# given ans
# 使用 heap 或 bucket sort

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))



