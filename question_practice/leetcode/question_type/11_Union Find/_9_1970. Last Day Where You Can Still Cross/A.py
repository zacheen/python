# 1970. Last Day Where You Can Still Cross
# https://leetcode.com/problems/last-day-where-you-can-still-cross

from typing import List
from math import inf

# my modify template UF_no_init : 160ms Beats94.93%
    # 只要左邊可以連到右邊(包括斜的)，就可以過
word_d = set(["L", "R"])
class UF_no_init:
    def __init__(self):
        self.id = {}                # <適用各種type> 多的
        self.linked = False

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        # 在 word_d 裡面的，一定是給別人的
        if u_is_w := u in word_d :
            self.id[v] = u
        else:
            self.id[u] = v
        if u_is_w and v in word_d:
            self.linked = True
            return

    def find(self, up):
        while up in self.id and up != (deep:=self.id[up]):
            self.id[up] = up = self.id[deep] if deep in self.id else deep
        return up

dir_list = [(0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0), (-1,1)]
class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        seen = [[True]+[False]*(col)+[True] for _ in range(row+2)]
        uf = UF_no_init()
        # 先把左右兩邊 各自union到 "L" 跟 "R"
        for i in range(row+2):
            uf.union((i,0), "L")
            uf.union((i,col+1), "R")
        
        for cou, (i1, i2) in enumerate(cells) :
            seen[i1][i2] = True
            # 跟周圍其他的格子 union
            for d1, d2 in dir_list :
                n1=i1+d1
                n2=i2+d2
                if seen[n1][n2]:
                    uf.union((n1,n2), (i1, i2))
            if uf.linked:
                return cou
        raise ValueError("No path found")

s = Solution()
print("ans :",s.latestDayToCross(row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]])) # 2
print("ans :",s.latestDayToCross(row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]])) # 1
print("ans :",s.latestDayToCross(row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]])) # 3



