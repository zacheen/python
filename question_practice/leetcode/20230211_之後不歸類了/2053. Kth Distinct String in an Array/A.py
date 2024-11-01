# 
# 

from typing import List
import functools

from collections import Counter
# my 
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        for key, val in c.items():
            if val == 1 :
                k -= 1
                if k == 0 :
                    return key
        return ""

# given ans
# same concept, slower but less change get error
class Solution:
  def kthDistinct(self, arr: List[str], k: int) -> str:
    count = Counter(arr)

    for a in arr:
      if count[a] == 1:
        k -= 1
        if k == 0:
          return a

    return ''
  
s = Solution()
print("ans :",s.kthDistinct(arr = ["d","b","c","b","c","a"], k = 2))
print("ans :",s.kthDistinct(arr = ["aaa","aa","a"], k = 1))
print("ans :",s.kthDistinct(arr = ["a","b","a"], k = 3))



