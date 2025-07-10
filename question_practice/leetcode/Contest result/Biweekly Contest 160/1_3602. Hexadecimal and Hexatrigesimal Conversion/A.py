# 3602. Hexadecimal and Hexatrigesimal Conversion
# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description/

from typing import List
from math import inf

# my 0ms
class Solution:
    def concatHex36(self, n: int) -> str:
        ord_a = ord("A")
        int_to_c = {i+10 : chr(i+ord_a) for i in range(26)}
        for i in range(10):
            int_to_c[i] = str(i)
        
        ans = []
        def turn(n, base):
            while n :
                ans.append(int_to_c[n%base])
                n = n//base
            
        turn(n**3,36)
        turn(n**2,16)
        return "".join(ans[::-1])

s = Solution()
print("ans :",s.concatHex36(13)) # A91P1
print("ans :",s.concatHex36(36)) # 5101000



