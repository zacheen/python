# 2429. Minimize XOR
# https://leetcode.com/problems/minimize-xor/description

from typing import List
import functools

# my 
def bin_to_n(st):
    ret_n = 0
    for c in st :
        ret_n = ret_n*2 + c
    print("bin_to_n", st, ret_n)
    return ret_n

def n_to_bin(n):
    print("n_to_bin", n, end=" ")
    ret_bit = []
    while n :
        if n & 1 :
            ret_bit.insert(0,1)
        else :
            ret_bit.insert(0,0)
        n = n >> 1
    print(ret_bit)
    return ret_bit

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        if num2 == 0 :
            return num1
        
        count_1 = sum(n_to_bin(num2))
        num1_bit = n_to_bin(num1)

        ans = [0]*len(num1_bit)
        for i in range(len(num1_bit)) :
            if num1_bit[i] == 1 :
                ans[i] = 1
                count_1 -= 1
                if count_1 == 0 :
                    return bin_to_n(ans)
        print("mid",ans)
        for i in range(len(ans)-1, -1, -1) :
            if ans[i] == 0 :
                ans[i] = 1
                count_1 -= 1
                if count_1 == 0 :
                    return bin_to_n(ans)
        while count_1 > 0 :
            ans.insert(0,1)
            count_1 -= 1
        return bin_to_n(ans)

# given ans

s = Solution()
# print("ans :",s.minimizeXor(3, 5)) # 3
# print("ans :",s.minimizeXor(1, 12)) # 3
# print("ans :",s.minimizeXor(25, 72)) # 24
print("ans :",s.minimizeXor(65, 84)) # 67



