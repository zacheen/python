# 3470. Permutations IV
# https://leetcode.com/problems/permutations-iv/description/

from typing import List
from math import inf

# my 47ms Beats100.00%
mem_fact = [1,1]
def fact(n) :
    while len(mem_fact) <= n :
        mem_fact.append( mem_fact[-1]*(len(mem_fact)) )
    return mem_fact[n]

from sortedcontainers import SortedSet
class Solution:
    def permute(self, n: int, k: int) -> List[int]:
        unused = SortedSet(range(1,n+1))
        ini_odd = (n%2 == 1)
        ans = []
        for remain_n in range(n-1,-1, -1) :
            if remain_n%2 == 0 :
                cout_comb = fact(remain_n//2)*fact(remain_n//2)
                for poss_n in unused :
                    if (ini_odd and poss_n%2 == 0) or (ans and poss_n&1 == ans[-1]&1) :
                        continue
                    if k <= cout_comb :
                        ans.append(poss_n)
                        unused.remove(poss_n)
                        break
                    else :
                        k -= cout_comb
            else :
                fewer = (remain_n-1)//2
                cout_comb = fact(fewer+1)*fact(fewer)
                for poss_n in unused :
                    if ans and poss_n&1 == ans[-1]&1 :
                        continue
                    if k <= cout_comb :
                        ans.append(poss_n)
                        unused.remove(poss_n)
                        break
                    else :
                        k -= cout_comb
        if len(ans) == n :
            return ans
        else :
            return []

# given ans : similar concept, but mine is simpler

s = Solution()
print("ans :",s.permute(4,6)) # [3,4,1,2]
print("ans :",s.permute(3,2)) # [3,2,1]
print("ans :",s.permute(2,3)) # []



