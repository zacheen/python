# 2048. Next Greater Numerically Balanced Number
# https://leetcode.com/problems/next-greater-numerically-balanced-number

from typing import List
from math import inf
from bisect import bisect_right

# my : 0ms
max_n = 7 # since 7777777 can cover all input range

all_set = set([(0,0)])
for i in range(1, max_n+1):
    now_bit = 1 << i
    for each_cnt, each_comb in all_set.copy() :
        if each_cnt+i <= max_n :
            all_set.add((each_cnt+i, each_comb|now_bit))

all_val_n = set()
def gen_comb(now_n, rem_cnt) :
    if sum(rem_cnt) == 0 :
        all_val_n.add(now_n)

    # append n
    for i in range(1,max_n+1) :
        if rem_cnt[i] :
            rem_cnt[i] -= 1
            gen_comb(now_n*10 + i, rem_cnt)
            rem_cnt[i] += 1

for each_cnt, each_comb in all_set :
    cnt = [0]*(max_n+1)
    for i in range(1, max_n+1):
        if each_comb & (1 << i) :
            cnt[i] += i
    gen_comb(0, cnt)

all_val_n = sorted(all_val_n)
# print(all_val_n)

class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        ret_i = bisect_right(all_val_n, n)
        return all_val_n[ret_i]
        
        

s = Solution()
print("ans :",s.nextBeautifulNumber(1)) # 22
print("ans :",s.nextBeautifulNumber(1000)) # 1333
print("ans :",s.nextBeautifulNumber(3000)) # 3133
print("ans :",s.nextBeautifulNumber(748601)) # 1224444
