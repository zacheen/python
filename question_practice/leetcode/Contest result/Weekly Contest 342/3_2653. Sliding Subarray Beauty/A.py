from typing import List
import functools

# my 
    # Bug 一次 
        # 第一個 sort_list[x] 忘記判斷有沒有大於 k
# 5897 ms Beats 25%
from sortedcontainers import SortedList
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        x = x-1 # because base 0
        sort_list = SortedList(nums[:k])
        ans = []
        if sort_list[x] > 0 :
            ans.append(0)
        else :
            ans.append(sort_list[x])
        for i in range(k, len(nums)) :
            sort_list.remove(nums[i-k])
            sort_list.add(nums[i])
            now_ans = sort_list[x]
            if now_ans > 0 :
                now_ans = 0
            ans.append(now_ans)
        return ans

# # given ans 
    # 有再優化 4573 ms Beats 25%
# 是用 hash 去計算各個項目有幾個 (因為範圍在 -50~50 之間)
# 如果 -50~50 的範圍再更大的話 def f() 裡面應該要用 binary search
class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        shift = 50 # 這是因為數值有負的 所以要全部平移到正的數值
        for i in range(len(nums)) :
            nums[i] += shift

        count = [0] * (2 * shift + 1)
        def f():
            s = 0
            for i in range(shift): # 這裡只有到 shift 是因為其他就是正的了
                s += count[i]
                if s >= x:
                    return i - shift
            return 0
        res = []
        for n in nums[:k]:
            count[n] += 1
        res.append(f())
        for i in range(k, len(nums)):
            count[nums[i]] += 1
            count[nums[i - k]] -= 1
            res.append(f())
        return res

s = Solution()
print(s.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2))
print(s.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2))
print(s.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))



