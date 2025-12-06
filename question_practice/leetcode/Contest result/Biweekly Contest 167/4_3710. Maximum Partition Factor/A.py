# 3710. Maximum Partition Factor
# https://leetcode.com/problems/maximum-partition-factor/description/

from typing import List
from math import inf
from collections import defaultdict

# my
class UF_Parity:
    def __init__(self, n):
        self.id = list(range(n))
        self.set_member_cnt = [1]*n    # <計算各個 set 的個數> 多的
        self.x = [0]*n

    def union(self, n1, n2, w = 1):
        f_n1 = self.find(n1)
        f_n2 = self.find(n2)
        if f_n1 == f_n2:
            return (self.x[n1] ^ self.x[n2]) == w
        if self.set_member_cnt[f_n1] > self.set_member_cnt[f_n2] : #  <Union by size> 多的
            f_n1,f_n2 = f_n2,f_n1
            n1, n2 = n2, n1
        # merge f_n1 into f_n2
        self.id[f_n1] = f_n2
        self.x[f_n1] = (self.x[n1] ^ self.x[n2] ^ w)
        self.set_member_cnt[f_n2] += self.set_member_cnt[f_n1]  # <計算各個 set 的個數> 多的
        return True

    def find(self, up):
        # To maintain Parity here can't use Half Path Compression
        if self.id[up] != up:
            deep = self.find(self.id[up])
            self.x[up] ^= self.x[self.id[up]]
            self.id[up] = deep
        return self.id[up]

# version 1 : 678ms Beats96.97%
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        # maximum possible partition factor over all valid splits
        
        all_edge = []
        for p1i, (p1x,p1y) in enumerate(points):
            for p2i, (p2x,p2y) in enumerate(points[:p1i]):
                dis = abs(p1x-p2x) + abs(p1y-p2y)
                all_edge.append((dis, p1i, p2i))
        
        uf = UF_Parity(len(points))
        all_edge.sort()
        for dis, p1i, p2i in all_edge :
            if not uf.union(p1i, p2i) :
                return dis
        return 0

# version 2 : 715ms Beats94.72%
    # would be faster if many collision in dis (dense connection)
class Solution:
    def maxPartitionFactor(self, points: List[List[int]]) -> int:
        # maximum possible partition factor over all valid splits
        
        dis_bucket = defaultdict(list)
        for p1i, (p1x,p1y) in enumerate(points):
            for p2i, (p2x,p2y) in enumerate(points[:p1i]):
                dis = abs(p1x-p2x) + abs(p1y-p2y)
                dis_bucket[dis].append((p1i, p2i))
        
        uf = UF_Parity(len(points))
        for dis in sorted(dis_bucket.keys()):
            for p1i, p2i in dis_bucket[dis] :
                # when I want to seperate p1i, p2i into two different set, it fails
                if not uf.union(p1i, p2i) :
                    return dis
        return 0

s = Solution()
print("ans :",s.maxPartitionFactor( [[0,0],[0,2],[2,0],[2,2]])) # 4
print("ans :",s.maxPartitionFactor( [[0,0],[0,1],[10,0]])) # 11

