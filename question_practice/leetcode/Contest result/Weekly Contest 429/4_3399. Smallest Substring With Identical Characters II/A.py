# 3399. Smallest Substring With Identical Characters II
# https://leetcode.com/problems/smallest-substring-with-identical-characters-ii/

from typing import List
import functools

# my 323ms Beats78.52%
# same as # 3398. Smallest Substring With Identical Characters I
class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        # checking len 1
        len_1_fail_count = 0
        # and count interval
        prev = s[0]
        last_c = 0
        count_list = []
        for i, c in enumerate(s) :
            # checking len 1
            len_1_fail_count += (i&1) ^ int(c)
            # count interval
            if c != prev :
                count_list.append(i-last_c)
                prev = c
                last_c = i
        count_list.append(len(s)-last_c)
        # print("count_list",count_list)
        # print("len_1_fail_count",len_1_fail_count)
        
        # return if len can be 1
        if len_1_fail_count <= numOps or (len(s)-len_1_fail_count) <= numOps :
            return 1

        # binary search 判斷哪個數符合條件
        left, right = 2, len(s) # right 通常會超出界線(因為執行的時候不會執行到這個數字) # 但是最後 l 有可能會超出範圍
        while left < right:
            mid = (left + right) // 2
            # mid OK or not
            if sum( n // (mid+1) for n in count_list ) > numOps: # 條件 (如果 == target 的情況 要是 False)
                # 沒通過 或 數字應該要往大的方向跑(目標沒有在 left 跟 mid 之間)
                left = mid + 1
            else:
                # 通過(包含 == target 的情況)
                right = mid 
        return left

# given ans

s = Solution()
print(s.minLength())



