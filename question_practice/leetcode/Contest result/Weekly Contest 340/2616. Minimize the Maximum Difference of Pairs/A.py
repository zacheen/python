# my 
from typing import List
import functools

# given ans Beats 40%
# binary search :
    # 檢測 c 這個距離，能不能夠有足夠的 distance 可以符合條件
        # 因為已經 sort ，所以可以 greedy
            # n1, n2, n3 
            # 不知道 (n2-n1) ? (n3-n2)
            # 但是絕對 (n2-n1) < (n3-n1)
            # 所以如果 (n2-n1) 符合條件，絕對就可以符合
class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        a = 0
        b = nums[-1]-nums[0]
        while a < b :
            c = (a + b) // 2
            ct = 0
            i = 0
            while i < len(nums)-1 :
                if (nums[i + 1] - nums[i]) <= c :
                    ct += 1
                    # 這個是因為符合條件 所以 i 跟 i+1 都取用了
                    i  += 1
                i += 1
            if ct >= p : 
                b = c
            else : 
                a = c + 1
        return a
    
# OK 我發現問題了 原來用過的 index 不能夠再使用
# [3,5,2,2,2,2]
    # (2,3) (4,5) 不能夠再 (2,4)

s = Solution()
print(s.minimizeMax(nums = [10,1,2,7,1,3], p = 2))
print(s.minimizeMax(nums = [4,2,1,2], p = 1))
print(s.minimizeMax(nums = [3,4,2,3,2,1,2], p = 3))
print(s.minimizeMax(nums = [3,4,2,3,2,2,2], p = 3))
print(s.minimizeMax(nums = [3,5,2,2,2,2], p = 3))



