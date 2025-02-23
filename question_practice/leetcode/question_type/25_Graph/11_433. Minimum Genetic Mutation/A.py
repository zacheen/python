# 433. Minimum Genetic Mutation
# https://leetcode.com/problems/minimum-genetic-mutation

from typing import List
from math import inf

from collections import defaultdict
# my 0ms Beats100.00%
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        li = defaultdict(list)
        for i, s1 in enumerate(bank):
            for s2 in bank[:i] :
                if sum(c1 != c2 for c1,c2 in zip(s1,s2)) == 1 :
                    li[s1].append(s2)
                    li[s2].append(s1)

        q = []
        seen = set()
        for b in bank :
            if sum(c1 != c2 for c1,c2 in zip(b,startGene)) == 1 :
                q.append(b)
                seen.add(b)
        
        ans_cou = 1
        while q :
            new_q = []
            for now_g in q :
                if now_g == endGene :
                    return ans_cou
                seen.add(now_g)
                for next_g in li[now_g] :
                    if next_g not in seen :
                        new_q.append(next_g)
            q = new_q
            ans_cou += 1
        return -1

# given ans


s = Solution()
# print("ans :",s.minMutation(startGene = "AACCGGTT", endGene = "AACCGGTA", bank = ["AACCGGTA"])) # 1
print("ans :",s.minMutation(startGene = "AACCGGTT", endGene = "AAACGGTA", bank = ["AACCGGTA","AACCGCTA","AAACGGTA"])) # 2



