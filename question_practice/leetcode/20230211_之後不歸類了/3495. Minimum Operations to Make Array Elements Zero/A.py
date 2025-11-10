# 3495. Minimum Operations to Make Array Elements Zero
# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero

from typing import List
from math import inf
from functools import cache

# my : 827ms Beats89.48%
# floor(a / 4) -> shift 2
def cal_repl(n):
    ret = 0
    while n != 0 :
        n >>= 2
        ret += 1
    return ret

@cache
def cal_2_exp(n):
    # 2**n ~ 2**(n+1)-1
    n = (n-1)*2
    first_n = 1<<n
    last_n = (1<<(n+2))-1
    return first_n, last_n
 
def cal_total_rep(st, en):
    i = 0
    cnt = 0
    while True :
        i += 1
        now_st, now_en = cal_2_exp(i)
        if now_st > en : # 沒有重疊
            break
        if st > now_en : # 沒有重疊
            continue
        if st > now_st : now_st = st
        if en < now_en : now_en = en
        cnt += (now_en - now_st + 1)*i
    return cnt

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # calculate the amount of count of the operation needed
        ans = 0
        for st, en in queries :
            if en-st <= 1 :
                ans += cal_repl(en)
            else :
                ans += (cal_total_rep(st,en)+1)//2 
        return ans
    
# inspire by given ans : 684ms Beats91.27%
# floor(a / 4) -> shift 2
def cal_repl(n):
    ret = 0
    while n != 0 :
        n >>= 2
        ret += 1
    return ret

@cache
def cal_2_exp(n):
    if n == 0 :
        return 0, 0
    # 2**n ~ 2**(n+1)-1
    n = (n-1)*2
    first_n = 1<<n
    last_n = (1<<(n+2))-1
    return first_n, last_n

@cache
def pre_rep(n):
    if n <= 0 :
        return 0
    first_n, last_n = cal_2_exp(n)
    return (last_n-first_n+1)*n + pre_rep(n-1)

def cal_total_rep(n):
    top_rep = cal_repl(n)
    
    fir_n, last_n = cal_2_exp(top_rep)
    last_n = n
    pre_cnt = pre_rep(top_rep-1)
    return (last_n - fir_n + 1)*top_rep + pre_cnt

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        # calculate the amount of count of the operation needed
        ans = 0
        for st, en in queries :
            if en-st <= 1 :
                ans += cal_repl(en)
            else :
                ans += (cal_total_rep(en)-cal_total_rep(st-1)+1)//2
        return ans

s = Solution()
# print("ans :",s.minOperations([[1,2],[2,4]])) # 3
# print("ans :",s.minOperations([[2,6]])) # 4
# print("ans :",s.minOperations([[6,8]])) # 3
print("ans :",s.minOperations([[1,8]])) # 3



