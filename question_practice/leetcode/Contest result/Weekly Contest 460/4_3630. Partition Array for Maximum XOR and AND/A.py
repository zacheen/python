# 3630. Partition Array for Maximum XOR and AND
# https://leetcode.com/problems/partition-array-for-maximum-xor-and-and/

from typing import List
from math import inf

# my 
class XorBasis:
    def __init__(self, n: int):
        self.b = [0] * (n.bit_length() + 1)
        # b[i] : 最高位i 代表的基

    def insert(self, x: int) -> None: # 回傳是否為新的項目
        b = self.b
        while x:
            i = x.bit_length()  # x 的最高位
            if b[i] == 0:       # x 和之前的基是線性無關的
                b[i] = x        # 新增一個基，最高位為 i
                return True
            x ^= b[i]           # 確保參與 max_xor 的基的最高位是互不相同的，方便我們貪心
        
        # 正常循環結束，此時 x=0，說明一開始的 x 可以被已有基表出，不是一個線性無關基
        return False

    def max_xor(self) -> int:
        res = 0
        # 從高到低貪心：越高的位，越必須是 1
        # 由於每個位的基至多一個，所以每個位只需考慮異或一個基，若能變大，則異或之
        for base_n in self.b[::-1]:
            if (new_res := res ^ base_n) > res:
                res = new_res
        return res
    
class Solution:
    def maximizeXorAndXor(self, nums: List[int]) -> int:
        n = len(nums)
        max_n = max(nums)

        u = 1 << n
        sub_and = [0] * u
        sub_xor = [0] * u
        sub_and[0] = -1
        for i, x in enumerate(nums):
            high_bit = 1 << i
            for mask in range(high_bit):
                sub_and[high_bit | mask] = sub_and[mask] & x
                sub_xor[high_bit | mask] = sub_xor[mask] ^ x
        sub_and[0] = 0

        def max_xor2(sub: int) -> int:
            b = XorBasis(max_n)
            xor = sub_xor[sub]
            for i, x in enumerate(nums):
                if sub >> i & 1:
                    b.insert(x & ~xor)
            return xor + b.max_xor() * 2

        return max(sub_and[i] + max_xor2((u - 1) ^ i) for i in range(u))


s = Solution()
print("ans :",s.maximizeXorAndXor([2,3])) # 5
print("ans :",s.maximizeXorAndXor([1,3,2])) # 6
print("ans :",s.maximizeXorAndXor([2,3,6,7])) # 15

