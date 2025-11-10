# 1733. Minimum Number of People to Teach
# https://leetcode.com/problems/minimum-number-of-people-to-teach

from typing import List
from math import inf
from collections import defaultdict

# my 
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        languages = list(set(l) for l in languages)

        # finding the friends that cannot talk to each other
        need_learn = set()
        for f1,f2 in friendships :
            f1 -= 1
            f2 -= 1
            if languages[f1] & languages[f2] :
                continue
            need_learn.add(f1)
            need_learn.add(f2)
        
        cnt = defaultdict(int)
        for p in need_learn :
            for l in languages[p] :
                cnt[l] += 1
        return len(need_learn) - max(cnt.values(), default = 0)
            
        
            

s = Solution()
print("ans :",s.minimumTeachings(n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]])) # 
print("ans :",s.minimumTeachings(n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]])) # 
# print("ans :",s.minimumTeachings()) # 



