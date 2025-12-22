# 2092. Find All People With Secret
# https://leetcode.com/problems/find-all-people-with-secret

from typing import List
from math import inf
from collections import defaultdict

# my v2
class UF_no_init:
    def __init__(self):
        self.id = {}                # <適用各種type> 多的

    def union(self, u, v):
        u = self.find(u)
        v = self.find(v)
        if u == v:
            return
        self.id[u] = v
        self.id[v] = v

    def find(self, up):
        while up in self.id and up != (deep := self.id[up]):
            self.id[up] = up = (self.id[deep] if deep in self.id else deep)
        return up

class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        meetings.sort(key = lambda x : x[2])
        meetings.append((-1,-1,inf))

        uf = UF_no_init()
        uf.union(0, firstPerson)
        seen = set()
        last_t = 0
        for p1,p2,t in meetings :
            if last_t != t :
                last_t = t
                root = uf.find(0)
                for p in seen :
                    if uf.find(p) != root :
                        del(uf.id[p])
                seen = set()
            seen.add(p1)
            seen.add(p2)
            uf.union(p1,p2)

        return list(uf.id.keys())
    
# my : time limit exceeded
# class UF_find_relate_no_init:
#     def __init__(self):
#         self.id = {}
#         self.set_member = {}

#     def union(self, n1, n2):
#         r_n1 = self.find(n1)
#         r_n2 = self.find(n2)
#         if n1==r_n1 and (r_n1 not in self.set_member) :
#             self.id[n1] = n1
#             self.set_member[r_n1] = set([r_n1])
#         if n2==r_n2 and (r_n2 not in self.set_member) :
#             self.id[n2] = n2
#             self.set_member[r_n2] = set([r_n2])
        
#         if r_n1 == r_n2:
#             return
#         self.set_member[r_n2] = self.set_member[r_n2] | self.set_member[r_n1]
#         self.set_member[r_n1] = None
#         self.id[r_n1] = r_n2

#     def find(self, up):
#         while up in self.id and up != (deep := self.id[up]):
#             self.id[up] = up = (self.id[deep] if deep in self.id else deep)
#         return up

#     def ger_related(self, u):
#         if self.id[u] != u:
#             self.id[u] = self.find(self.id[u])
#         return self.set_member[self.id[u]]

# class Solution:
#     def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
#         meetings.sort(key = lambda x : x[2])
#         # print(meetings)

#         last_t = 0
#         last_uf = UF_find_relate_no_init()
#         know_per = set([0, firstPerson])
#         meetings.append((-1,-1,inf))
#         for p1,p2,t in meetings :
#             if t != last_t :
#                 for each_g in last_uf.id.keys() :
#                     if last_uf.find(each_g) == each_g :
#                         this_group = last_uf.ger_related(each_g)
#                         # check any one in this group know the secret
#                         spread = False
#                         for each_p in this_group :
#                             if each_p in know_per :
#                                 spread = True
#                                 break
#                         # print("spread", spread, this_group)
#                         if spread :
#                             know_per |= set(this_group)
#                 # clean
#                 last_t = t
#                 last_uf = UF_find_relate_no_init()
#             last_uf.union(p1,p2)
                
#         return list(know_per)

s = Solution()
print("ans :",s.findAllPeople(n = 6, meetings = [[1,2,5],[2,3,8],[1,5,10]], firstPerson = 1)) # 
print("ans :",s.findAllPeople(n = 4, meetings = [[3,1,3],[1,2,2],[0,3,3]], firstPerson = 3)) # 
print("ans :",s.findAllPeople(n = 5, meetings = [[3,4,2],[1,2,1],[2,3,1]], firstPerson = 1)) # 
