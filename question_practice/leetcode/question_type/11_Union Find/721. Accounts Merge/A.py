# 721. Accounts Merge
# https://leetcode.com/problems/accounts-merge/description/

from typing import List
from math import inf

# my 23ms Beats79.46%
class UF:
    def __init__(self, n):
        self.id = list(range(n))

    def union(self, u, v):
        i = self.find(u)
        j = self.find(v)
        if i == j:
            return
        if i < j :
            self.id[j] = i
        else :
            self.id[i] = j

    def find(self, u):
        if self.id[u] != u:
            self.id[u] = self.find(self.id[u])
        return self.id[u]

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UF(len(accounts))
        mem = {}
        for indx, info in enumerate(accounts) :
            for email in info[1:] :
                if email in mem :
                    uf.union(indx, mem[email])
                else :
                    mem[email] = indx

        for indx in range(len(accounts)) :
            uf.find(indx)
        
        ans = []
        for indx, info in enumerate(accounts) :
            if uf.find(indx) != indx :
                ans.append([])
                pre_info = ans[uf.find(indx)][1]
                pre_info |= set(info[1:])
            else :
                ans.append([info[0], set(info[1:])])
        return [[a[0]]+sorted(a[1]) for a in ans if len(a) > 0]

# given ans
# directly union emails in "def union"

from collections import defaultdict
# given ans 2 : 21ms Beats84.17%
# using DFS
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_idx = defaultdict(list)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_idx[email].append(i)

        def dfs(i: int) -> None:
            vis[i] = True
            for email in accounts[i][1:]:  # 遍历 i 的所有邮箱地址
                if email in email_set:
                    continue
                email_set.add(email)
                for j in email_to_idx[email]:  # 遍历所有包含该邮箱地址的账户下标 j
                    if not vis[j]:  # j 没有访问过
                        dfs(j)

        ans = []
        vis = [False] * len(accounts)
        for i, b in enumerate(vis):
            if not b:  # i 没有访问过
                email_set = set()  # 用于收集 DFS 中访问到的邮箱地址
                dfs(i)
                ans.append([accounts[i][0]] + sorted(email_set))
        return ans


s = Solution()
# print("ans :",s.accountsMerge(accounts = [
#     ["John","johnsmith@mail.com","john_newyork@mail.com"],
#     ["John","johnsmith@mail.com","john00@mail.com"],
#     ["Mary","mary@mail.com"],
#     ["John","johnnybravo@mail.com"]])) # 
print("ans :",s.accountsMerge(accounts = [
    ["David","David0@m.co","David1@m.co"],
    ["David","David3@m.co","David4@m.co"],
    ["David","David4@m.co","David5@m.co"],
    ["David","David2@m.co","David3@m.co"],
    ["David","David1@m.co","David2@m.co"]])) # 



