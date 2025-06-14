# 2818. Apply Operations to Maximize Score
# https://leetcode.com/problems/apply-operations-to-maximize-score

from typing import List
from math import inf

# my 547ms Beats96.49%
MOD = 10**9 + 7
MAX = 10 ** 5 + 1
fac = [[] for _ in range(MAX)]
for i in range(2, MAX):
    if len(fac[i]) == 0 : 
        for j in range(i, MAX, i):
            fac[j].append(i)

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        pri_sc = [len(fac[n]) for n in nums]
        l_c = [0]*len(nums)
        r_c = [0]*len(nums)
        
        stack = [] # stack[i][0] should be strict decrease 
        for i, n in enumerate(pri_sc) :
            cou = 1
            while stack and n > stack[-1][0] :
                cou += stack.pop()[1]
            if stack and n == stack[-1][0] :
                stack[-1][1] += cou
            else :
                stack.append([n,cou])
            l_c[i] = cou

        stack = [] # stack[i][0] should be strict decrease 
        for i, n in reversed(list(enumerate(pri_sc))) :
            cou = 1
            while stack and n >= stack[-1][0] :
                cou += stack.pop()[1]
            stack.append([n,cou])
            r_c[i] = cou
        
        comb = [(n, l, r) for n, l, r in zip(nums, l_c, r_c)]
        comb.sort(key= lambda x:-x[0])
        ans = 1
        for n, l, r in comb :
            if (com_num := l*r) < k :
                ans = ans*pow(n, com_num, MOD) % MOD
                k -= com_num
            else :
                ans = ans*pow(n, k, MOD) % MOD
                return ans
        return ans

# given ans


s = Solution()
print("ans :",s.maximumScore(nums = [8,3,9,3,8], k = 2)) # 
print("ans :",s.maximumScore(nums = [19,12,14,6,10,18], k = 3)) # 
print("ans :",s.maximumScore(nums = [2,6,30,6,30,210,30,6,30,6,2], k = 3)) # 



