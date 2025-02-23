# 864. Shortest Path to Get All Keys
# 

from typing import List
from math import inf

from collections import defaultdict
# my : 103ms Beats93.81%
key_to_num = {chr(c) : 1<<n for c,n in zip(range(ord("a"), ord("a")+6), range(6))}
lock_to_num = {chr(c) : 1<<n for c,n in zip(range(ord("A"), ord("A")+6), range(6))}
# print(key_to_num)
class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        i1_len = len(grid)
        i2_len = len(grid[0])
        seen = [[set() for __ in range(i2_len)] for _ in range(i1_len)]

        # finding start point and key amount
        key_cou = 0
        for i1, l in enumerate(grid) :
            for i2, c in enumerate(l) :
                if c in key_to_num :
                    key_cou = (key_cou<<1) + 1
                elif c == "@" :
                    q = [(i1,i2,0)] # (i1,i2,status)
        # print("start_q :", q)
        # print("key_cou :", key_cou)
        
        dir_l = [(0,1),(1,0),(0,-1),(-1,0)]
        seen[0][0].add(0)
        step_cou = 1
        while q :
            new_q = []
            for i1,i2,status in q :
                for d1,d2 in dir_l :
                    nei1 = i1+d1
                    nei2 = i2+d2
                    if 0 <= nei1 < i1_len and 0 <= nei2 < i2_len :
                        this_c = grid[nei1][nei2]
                        if this_c == "#" :
                            # blocked by wall
                            continue
                        elif this_c in lock_to_num and status & lock_to_num[this_c] == 0:
                            # blocked by lock (don't have key)
                            continue
                        new_status = status
                        if this_c in key_to_num :
                            # get key
                            new_status |= key_to_num[this_c]
                            if new_status == key_cou :
                                return step_cou
                        if new_status not in seen[nei1][nei2] :
                            seen[nei1][nei2].add(new_status)
                            new_q.append((nei1,nei2,new_status))
            step_cou += 1
            q = new_q
        return -1

s = Solution()
print("ans :",s.shortestPathAllKeys(["@.a..","###.#","b.A.B"])) # 8
print("ans :",s.shortestPathAllKeys(["@..aA","..B#.","....b"])) # 6
print("ans :",s.shortestPathAllKeys(["@Aa"])) # -1



