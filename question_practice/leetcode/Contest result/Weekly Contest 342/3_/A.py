from typing import List
import functools

# my 
    # Bug 一次 
        # 第一個 sort_list[x] 忘記判斷有沒有大於 k

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

# given ans

s = Solution()
print(s.getSubarrayBeauty(nums = [1,-1,-3,-2,3], k = 3, x = 2))
print(s.getSubarrayBeauty(nums = [-1,-2,-3,-4,-5], k = 2, x = 2))
print(s.getSubarrayBeauty(nums = [-3,1,2,-3,0,-3], k = 2, x = 1))



