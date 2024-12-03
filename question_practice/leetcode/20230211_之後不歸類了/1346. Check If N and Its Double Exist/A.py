# 1346. Check If N and Its Double Exist

from typing import List
import functools

# my 0ms Beats 100.00%
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        exist_set = set()
        for each_i in arr :
            if each_i in exist_set :
                return True
            exist_set.add(each_i * 2)
            exist_set.add(each_i / 2)
        return False

# given ans

s = Solution()
print("ans :",s.checkIfExist([10,2,5,3]))
print("ans :",s.checkIfExist([3,1,7,11]))



