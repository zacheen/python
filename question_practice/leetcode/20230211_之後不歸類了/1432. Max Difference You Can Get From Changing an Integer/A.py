# 1432. Max Difference You Can Get From Changing an Integer
# https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer

from typing import List
from math import inf

# my 0ms
class Solution:
    def maxDiff(self, num: int) -> int:
        str_num = str(num)
        max_num = num
        for c in str_num :
            if c != '9' :
                max_num = int(str_num.replace(c,'9'))
                break
        
        min_num = num
        if str_num[0] != '1' :
            min_num = int(str_num.replace(str_num[0],'1'))
        else :
            for c in str_num[1:] :
                if c != '0' and c != '1':
                    min_num = int(str_num.replace(c,'0'))
                    break
        
        return max_num - min_num

s = Solution()
print("ans :",s.maxDiff(555)) # 888
print("ans :",s.maxDiff(9)) # 8
print("ans :",s.maxDiff(111)) # 888



