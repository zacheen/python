from collections import Counter
# my Runtime: 107 ms, faster than 86.33% of Python3
class Solution:
    def topKFrequent(self, nums, k):
        return [i[0] for i in Counter(nums).most_common(k)]

# given ans
# 使用 heap 或 bucket sort

s = Solution()
print(s.topKFrequent(nums = [1,1,1,2,2,3], k = 2))



