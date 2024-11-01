# my 先測試一下 sort 的速度 Beats 92.48%
class Solution(object):
    def sortArray(self, nums):
        nums.sort()
        return nums

# my 
# 比 sort 慢 795ms Beats79.81%
from collections import Counter
class Solution(object):
    def sortArray(self, nums):
        c = Counter(nums)
        ans = []
        for this_num in range(-50000, 50001):
            cou = c[this_num]
            for i in range(cou) :
                ans.append(this_num)
        return ans

# given ans

s = Solution()
print(s.sortArray())



